#!/usr/bin/env python3
"""
pass_persist.py
---------------
Resident pass_persist agent for snmpd.
Bridges odr-dabmux (ZMQ :12720) and odr-dabmod (Telnet :2120)
into an SNMP OID tree under .1.3.6.1.4.1.8072.1.3.2.99

OID layout
----------
.99.1.x  — mux subchannels (per subchannel, indexed 1-3)
  .1.1.x   sub-01
  .1.2.x   sub-02
  .1.3.x   sub-03
    .1  max_fill        (integer)
    .2  min_fill        (integer)
    .3  num_underruns   (counter)
    .4  num_overruns    (counter)
    .5  peak_left       (integer, dBfs * 100)
    .6  peak_right      (integer, dBfs * 100)
    .7  state           (string)
    .8  uptime          (integer, seconds)

.99.2.x  — mux outputs
  .1  num_connections   (integer)

.99.3.x  — mod stats
  .1  num_modulator_restarts   (counter)
  .2  most_recent_edi_decoded  (string)
  .3  edi_source               (string)
  .4  running_since            (string)
  .5  ensemble_label           (string)
  .6  ensemble_eid             (string)
  .7  num_services             (integer)
  .8  digital_gain             (string)
  .9  gainmode                 (string)
  .10 iq_samplerate            (integer)
  .11 tist_offset              (string)
"""

import sys
import json
import time
import socket
import threading
import zmq

# ─── Config ──────────────────────────────────────────────────────────────────

MUX_HOST = "mux"
MUX_ZMQ_PORT = 12720
MOD_HOST = "mod"
MOD_TELNET_PORT = 2120

BASE_OID = ".1.3.6.1.4.1.8072.1.3.2.99"

POLL_INTERVAL = 25          # seconds between background refreshes
CONNECT_RETRY  = 5          # seconds between reconnect attempts

# ─── Shared state ────────────────────────────────────────────────────────────

_lock  = threading.Lock()
_cache = {}          # oid_string -> (type_string, value_string)

# ─── Helpers ─────────────────────────────────────────────────────────────────

def oid(suffix):
    return BASE_OID + suffix

def _safe_int(v, scale=1):
    try:
        return int(float(v) * scale)
    except (TypeError, ValueError):
        return 0

def _safe_str(v):
    return str(v) if v is not None else ""

# ─── MUX collector ───────────────────────────────────────────────────────────

def collect_mux():
    ctx = zmq.Context()
    while True:
        s = None
        try:
            s = ctx.socket(zmq.REQ)
            s.setsockopt(zmq.RCVTIMEO, 3000)
            s.setsockopt(zmq.SNDTIMEO, 3000)
            s.setsockopt(zmq.LINGER, 0)
            s.connect(f"tcp://{MUX_HOST}:{MUX_ZMQ_PORT}")

            while True:
                s.send(b"values")
                values = json.loads(s.recv().decode()).get("values", {})
                s.send(b"output_values")
                outputs = json.loads(s.recv().decode()).get("output_values", {})

                new = {}

                # subchannels — map sorted keys to index 1,2,3...
                for idx, (ident, v) in enumerate(sorted(values.items()), start=1):
                    st = v.get("inputstat", {})
                    pfx = f".1.{idx}"
                    new[oid(f"{pfx}.1")] = ("INTEGER", _safe_int(st.get("max_fill")))
                    new[oid(f"{pfx}.2")] = ("INTEGER", _safe_int(st.get("min_fill")))
                    new[oid(f"{pfx}.3")] = ("Counter32", _safe_int(st.get("num_underruns")))
                    new[oid(f"{pfx}.4")] = ("Counter32", _safe_int(st.get("num_overruns")))
                    # peak levels are floats (dBfs), scale *100 to keep as integer
                    new[oid(f"{pfx}.5")] = ("INTEGER", _safe_int(st.get("peak_left"),  100))
                    new[oid(f"{pfx}.6")] = ("INTEGER", _safe_int(st.get("peak_right"), 100))
                    new[oid(f"{pfx}.7")] = ("STRING",  _safe_str(st.get("state")))
                    new[oid(f"{pfx}.8")] = ("INTEGER", _safe_int(st.get("uptime")))

                # outputs
                for idx, (k, v) in enumerate(sorted(outputs.items()), start=1):
                    new[oid(f".2.{idx}")] = ("INTEGER", _safe_int(v.get("num_connections")))

                with _lock:
                    _cache.update(new)

                time.sleep(POLL_INTERVAL)

        except Exception:
            pass
        finally:
            if s:
                s.close()
        time.sleep(CONNECT_RETRY)


# ─── MOD collector ───────────────────────────────────────────────────────────

def _telnet_read_prompt(sock):
    buf = ""
    while True:
        chunk = sock.recv(4096).decode(errors="replace")
        buf += chunk
        if buf.strip().endswith(">"):
            break
    return buf

def _telnet_cmd(sock, cmd):
    sock.sendall((cmd + "\n").encode())
    raw = _telnet_read_prompt(sock)
    lines = raw.strip().splitlines()
    # last line is the prompt; second-to-last is the response
    for line in reversed(lines):
        line = line.strip().rstrip(">").strip()
        if line:
            return line
    return ""

def collect_mod():
    while True:
        sock = None
        try:
            sock = socket.socket()
            sock.settimeout(4)
            sock.connect((MOD_HOST, MOD_TELNET_PORT))
            _telnet_read_prompt(sock)   # consume banner

            while True:
                raw = {
                    "num_modulator_restarts":  _telnet_cmd(sock, "get mainloop num_modulator_restarts"),
                    "most_recent_edi_decoded": _telnet_cmd(sock, "get mainloop most_recent_edi_decoded"),
                    "edi_source":              _telnet_cmd(sock, "get mainloop edi_source"),
                    "running_since":           _telnet_cmd(sock, "get mainloop running_since"),
                    "ensemble_label":          _telnet_cmd(sock, "get mainloop ensemble_label"),
                    "ensemble_eid":            _telnet_cmd(sock, "get mainloop ensemble_eid"),
                    "num_services":            _telnet_cmd(sock, "get mainloop num_services"),
                    "digital_gain":            _telnet_cmd(sock, "get gain digital"),
                    "gainmode":                _telnet_cmd(sock, "get gain mode"),
                    "iq_samplerate":           _telnet_cmd(sock, "get modulator rate"),
                    "tist_offset":             _telnet_cmd(sock, "get tist offset"),
                }

                new = {
                    oid(".3.1"):  ("Counter32", _safe_int(raw["num_modulator_restarts"])),
                    oid(".3.2"):  ("STRING",    _safe_str(raw["most_recent_edi_decoded"])),
                    oid(".3.3"):  ("STRING",    _safe_str(raw["edi_source"])),
                    oid(".3.4"):  ("STRING",    _safe_str(raw["running_since"])),
                    oid(".3.5"):  ("STRING",    _safe_str(raw["ensemble_label"])),
                    oid(".3.6"):  ("STRING",    _safe_str(raw["ensemble_eid"])),
                    oid(".3.7"):  ("INTEGER",   _safe_int(raw["num_services"])),
                    oid(".3.8"):  ("STRING",    _safe_str(raw["digital_gain"])),
                    oid(".3.9"):  ("STRING",    _safe_str(raw["gainmode"])),
                    oid(".3.10"): ("INTEGER",   _safe_int(raw["iq_samplerate"])),
                    oid(".3.11"): ("STRING",    _safe_str(raw["tist_offset"])),
                }

                with _lock:
                    _cache.update(new)

                time.sleep(POLL_INTERVAL)

        except Exception:
            pass
        finally:
            if sock:
                try:
                    sock.close()
                except Exception:
                    pass
        time.sleep(CONNECT_RETRY)


# ─── pass_persist protocol ───────────────────────────────────────────────────

def sorted_oids():
    """Return OIDs sorted numerically."""
    def oid_key(o):
        return [int(x) for x in o.lstrip(".").split(".")]
    with _lock:
        return sorted(_cache.keys(), key=oid_key)

def get_oid(oid_str):
    with _lock:
        return _cache.get(oid_str)

def get_next_oid(oid_str):
    keys = sorted_oids()
    for k in keys:
        if k > oid_str:
            return k
    return None

def respond(oid_str, entry):
    t, v = entry
    print(oid_str)
    print(t)
    print(v)
    sys.stdout.flush()

def none_response():
    print("NONE")
    sys.stdout.flush()

def main():
    # Start background collector threads
    t1 = threading.Thread(target=collect_mux, daemon=True)
    t2 = threading.Thread(target=collect_mod, daemon=True)
    t1.start()
    t2.start()

    # Give collectors a moment to populate cache on first start
    time.sleep(2)

    # pass_persist main loop — read commands from stdin
    for line in sys.stdin:
        cmd = line.strip().upper()

        if cmd == "PING":
            print("PONG")
            sys.stdout.flush()

        elif cmd == "GET":
            req_oid = sys.stdin.readline().strip()
            entry = get_oid(req_oid)
            if entry:
                respond(req_oid, entry)
            else:
                none_response()

        elif cmd == "GETNEXT":
            req_oid = sys.stdin.readline().strip()
            next_o = get_next_oid(req_oid)
            if next_o:
                entry = get_oid(next_o)
                respond(next_o, entry)
            else:
                none_response()

        elif cmd == "SET":
            sys.stdin.readline()   # oid
            sys.stdin.readline()   # type/value
            print("not-writable")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
