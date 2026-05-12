#!/usr/bin/env python3
"""
debug.py
--------
Run this inside the collector container for a human-readable
live view of all DAB stack stats.

Usage:
  python3 /collector/debug.py            # single snapshot
  python3 /collector/debug.py --loop 5  # refresh every 5 seconds
  python3 /collector/debug.py --loop 5 --compact  # terse one-liner per subchannel
"""

import json
import socket
import sys
import time
import argparse
import zmq
from datetime import datetime, timezone

MUX_HOST       = "mux"
MUX_ZMQ_PORT   = 12720
MOD_HOST       = "mod"
MOD_TELNET_PORT = 2120

# ─── ANSI colours ─────────────────────────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
RED    = "\033[31m"
CYAN   = "\033[36m"
DIM    = "\033[2m"

def col(text, colour):
    return f"{colour}{text}{RESET}"

def status_colour(state):
    if state is None:
        return DIM
    s = str(state).lower()
    if "ok" in s or "run" in s:
        return GREEN
    if "warn" in s or "prebuffer" in s:
        return YELLOW
    return RED

# ─── MUX query ────────────────────────────────────────────────────────────────

def query_mux():
    ctx = zmq.Context()
    s = ctx.socket(zmq.REQ)
    s.setsockopt(zmq.RCVTIMEO, 3000)
    s.setsockopt(zmq.SNDTIMEO, 3000)
    s.setsockopt(zmq.LINGER, 0)
    try:
        s.connect(f"tcp://{MUX_HOST}:{MUX_ZMQ_PORT}")
        s.send(b"info")
        info = json.loads(s.recv().decode())
        s.send(b"values")
        values = json.loads(s.recv().decode()).get("values", {})
        s.send(b"output_values")
        outputs = json.loads(s.recv().decode()).get("output_values", {})
        return info, values, outputs
    finally:
        s.close()
        ctx.term()

# ─── MOD query ────────────────────────────────────────────────────────────────

def _read_prompt(sock):
    buf = ""
    while True:
        chunk = sock.recv(4096).decode(errors="replace")
        buf += chunk
        if buf.strip().endswith(">"):
            break
    return buf

def _cmd(sock, cmd):
    sock.sendall((cmd + "\n").encode())
    raw = _read_prompt(sock)
    for line in reversed(raw.strip().splitlines()):
        line = line.strip().rstrip(">").strip()
        if line:
            return line
    return ""

def query_mod():
    sock = socket.socket()
    sock.settimeout(4)
    try:
        sock.connect((MOD_HOST, MOD_TELNET_PORT))
        _read_prompt(sock)
        return {
            "num_modulator_restarts":  _cmd(sock, "get mainloop num_modulator_restarts"),
            "most_recent_edi_decoded": _cmd(sock, "get mainloop most_recent_edi_decoded"),
            "edi_source":              _cmd(sock, "get mainloop edi_source"),
            "running_since":           _cmd(sock, "get mainloop running_since"),
            "ensemble_label":          _cmd(sock, "get mainloop ensemble_label"),
            "ensemble_eid":            _cmd(sock, "get mainloop ensemble_eid"),
            "num_services":            _cmd(sock, "get mainloop num_services"),
            "digital_gain":            _cmd(sock, "get gain digital"),
            "gainmode":                _cmd(sock, "get gain mode"),
            "iq_samplerate":           _cmd(sock, "get modulator rate"),
            "tist_offset":             _cmd(sock, "get tist offset"),
        }
    finally:
        sock.close()

# ─── Display ──────────────────────────────────────────────────────────────────

def bar(fill, width=20, max_val=100):
    try:
        pct = min(int(float(fill) / max_val * width), width)
    except (TypeError, ValueError):
        pct = 0
    colour = GREEN if pct > width * 0.5 else YELLOW if pct > width * 0.2 else RED
    return col("█" * pct + "░" * (width - pct), colour)

def print_full(info, values, outputs, mod):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"\n{col('━'*60, CYAN)}")
    print(f"  {col('DAB Stack Debug', BOLD)}  {col(ts, DIM)}")
    print(f"{col('━'*60, CYAN)}")

    # ── Mux ensemble ──
    svc = info.get("service", "?")
    print(f"\n  {col('MUX', BOLD)}  service={col(svc, CYAN)}")

    for ident, v in sorted(values.items()):
        st = v.get("inputstat", {})
        state    = st.get("state", "?")
        max_fill = st.get("max_fill", 0)
        min_fill = st.get("min_fill", 0)
        underruns= st.get("num_underruns", 0)
        overruns = st.get("num_overruns",  0)
        pl       = st.get("peak_left",  None)
        pr       = st.get("peak_right", None)
        uptime   = st.get("uptime",     0)

        state_col = status_colour(state)
        print(f"\n  {col(ident, BOLD)}")
        print(f"    State      : {col(state, state_col)}")
        print(f"    Buffer     : {bar(max_fill)} max={max_fill} min={min_fill}")
        print(f"    Underruns  : {col(str(underruns), RED if underruns else GREEN)}   "
              f"Overruns: {col(str(overruns), RED if overruns else GREEN)}")
        if pl is not None:
            print(f"    Peak L/R   : {pl:.1f} dBfs / {pr:.1f} dBfs")
        print(f"    Uptime     : {uptime}s")

    print(f"\n  {col('Outputs', BOLD)}")
    for k, v in sorted(outputs.items()):
        nc = v.get("num_connections", 0)
        print(f"    {k}: {col(str(nc), GREEN if nc else YELLOW)} connection(s)")

    # ── Mod ──
    print(f"\n  {col('MOD', BOLD)}")
    if "error" in mod:
        print(f"    {col('ERROR: ' + mod['error'], RED)}")
    else:
        restarts = int(mod.get("num_modulator_restarts", 0) or 0)
        print(f"    Ensemble   : {col(mod.get('ensemble_label','?'), CYAN)}  "
              f"EID={mod.get('ensemble_eid','?')}")
        print(f"    Services   : {mod.get('num_services','?')}")
        print(f"    EDI source : {mod.get('edi_source','?')}")
        print(f"    Last EDI   : {mod.get('most_recent_edi_decoded','?')}")
        print(f"    Running    : {mod.get('running_since','?')}")
        print(f"    Gain       : digital={mod.get('digital_gain','?')}  mode={mod.get('gainmode','?')}")
        print(f"    Sample rate: {mod.get('iq_samplerate','?')} Hz")
        print(f"    TIST offset: {mod.get('tist_offset','?')}")
        print(f"    Restarts   : {col(str(restarts), RED if restarts else GREEN)}")

    print(f"\n{col('━'*60, CYAN)}\n")

def print_compact(values, mod):
    ts = datetime.now().strftime("%H:%M:%S")
    parts = [col(ts, DIM)]
    for ident, v in sorted(values.items()):
        st = v.get("inputstat", {})
        state = st.get("state","?")
        uf    = st.get("num_underruns", 0)
        fill  = st.get("max_fill", 0)
        sc    = status_colour(state)
        parts.append(f"{col(ident, BOLD)}:{col(state,sc)} buf={fill} uf={col(str(uf), RED if uf else GREEN)}")
    if "error" not in mod:
        restarts = mod.get("num_modulator_restarts", "0")
        parts.append(f"mod_restarts={col(str(restarts), RED if int(restarts or 0) else GREEN)}")
    print("  ".join(parts))

# ─── Main ─────────────────────────────────────────────────────────────────────

def snapshot(compact=False):
    errors = []

    try:
        info, values, outputs = query_mux()
        mux_ok = True
    except Exception as e:
        info, values, outputs = {}, {}, {}
        mux_ok = False
        errors.append(f"MUX unreachable: {e}")

    try:
        mod = query_mod()
    except Exception as e:
        mod = {"error": str(e)}
        errors.append(f"MOD unreachable: {e}")

    if compact:
        print_compact(values, mod)
    else:
        print_full(info, values, outputs, mod)

    if errors and not compact:
        for err in errors:
            print(f"  {col('⚠ ' + err, YELLOW)}")

def main():
    parser = argparse.ArgumentParser(description="DAB stack debug tool")
    parser.add_argument("--loop", type=int, default=0,
                        help="Refresh interval in seconds (0 = run once)")
    parser.add_argument("--compact", action="store_true",
                        help="One-line-per-poll compact output")
    args = parser.parse_args()

    if args.loop > 0:
        print(f"{col('DAB debug live view', BOLD)} — refreshing every {args.loop}s  (Ctrl+C to stop)\n")
        try:
            while True:
                snapshot(args.compact)
                time.sleep(args.loop)
        except KeyboardInterrupt:
            print("\nStopped.")
    else:
        snapshot(args.compact)

if __name__ == "__main__":
    main()
