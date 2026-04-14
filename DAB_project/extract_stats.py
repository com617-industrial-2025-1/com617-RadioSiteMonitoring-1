#!/usr/bin/env python3
# extract_stats.py
# Pulls stats from odr-dabmux and odr-dabmod and saves as JSON.
#
# Usage:
#   sudo python3 extract_stats.py
#   sudo python3 extract_stats.py --loop 10

import json
import time
import os
import pwd
import argparse
import subprocess
from datetime import datetime, timezone

MUX_CONTAINER = "dab_mux"
MOD_CONTAINER = "dab_mod"
OUTPUT_MUX    = "stats_mux.json"
OUTPUT_MOD    = "stats_mod.json"

# Fix file ownership back to the real user after writing with sudo
REAL_USER = os.environ.get("SUDO_USER", os.environ.get("USER", "sebastian"))

MUX_QUERY = """
import zmq, json
ctx = zmq.Context()
s = ctx.socket(zmq.REQ)
s.setsockopt(zmq.RCVTIMEO, 2000)
s.connect('tcp://localhost:12720')
s.send(b'info')
info = json.loads(s.recv().decode())
s.send(b'values')
values = json.loads(s.recv().decode()).get('values', {})
s.send(b'output_values')
outputs = json.loads(s.recv().decode()).get('output_values', {})
inputs = {}
for ident, v in values.items():
    st = v.get('inputstat', {})
    inputs[ident] = {
        'max_fill': st.get('max_fill'),
        'min_fill': st.get('min_fill'),
        'num_underruns': st.get('num_underruns'),
        'num_overruns': st.get('num_overruns'),
        'peak_left': st.get('peak_left'),
        'peak_right': st.get('peak_right'),
        'state': st.get('state'),
        'uptime': st.get('uptime'),
    }
out = {}
for k, v in outputs.items():
    out[k] = {'num_connections': v.get('num_connections')}
print(json.dumps({'service': info.get('service',''), 'inputs': inputs, 'outputs': out}))
"""

MOD_QUERY = """
import socket, time, json
s = socket.socket()
s.settimeout(2)
s.connect(('localhost', 2120))
s.recv(4096)
def cmd(s, c):
    s.sendall((c + '\\n').encode())
    time.sleep(0.3)
    return s.recv(4096).decode().strip().split('\\n')[-1].replace('> ','').replace('>','').strip()
stats = {
    'num_modulator_restarts':  cmd(s, 'get mainloop num_modulator_restarts'),
    'most_recent_edi_decoded': cmd(s, 'get mainloop most_recent_edi_decoded'),
    'edi_source':              cmd(s, 'get mainloop edi_source'),
    'running_since':           cmd(s, 'get mainloop running_since'),
    'ensemble_label':          cmd(s, 'get mainloop ensemble_label'),
    'ensemble_eid':            cmd(s, 'get mainloop ensemble_eid'),
    'num_services':            cmd(s, 'get mainloop num_services'),
    'digital_gain':            cmd(s, 'get gain digital'),
    'gainmode':                cmd(s, 'get gain mode'),
    'iq_samplerate':           cmd(s, 'get modulator rate'),
    'tist_offset':             cmd(s, 'get tist offset'),
}
s.close()
print(json.dumps(stats))
"""

def docker_exec(container, query):
    try:
        result = subprocess.run(
            ["docker", "exec", container, "python3", "-c", query],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode != 0:
            return {"error": result.stderr.strip()}
        return json.loads(result.stdout.strip())
    except subprocess.TimeoutExpired:
        return {"error": f"timeout running docker exec on {container}"}
    except Exception as e:
        return {"error": str(e)}


def fix_ownership(filepath):
    """Give the file back to the real user if running under sudo."""
    try:
        uid = pwd.getpwnam(REAL_USER).pw_uid
        gid = pwd.getpwnam(REAL_USER).pw_gid
        os.chown(filepath, uid, gid)
    except Exception:
        pass


def collect_and_save():
    timestamp = datetime.now(timezone.utc).isoformat()
    print(f"[{timestamp}] Collecting stats...")

    mux_data = docker_exec(MUX_CONTAINER, MUX_QUERY)
    with open(OUTPUT_MUX, "w") as f:
        json.dump({"timestamp": timestamp, "source": MUX_CONTAINER, "stats": mux_data}, f, indent=2)
    fix_ownership(OUTPUT_MUX)
    print(f"  Mux stats  -> {OUTPUT_MUX}")

    mod_data = docker_exec(MOD_CONTAINER, MOD_QUERY)
    with open(OUTPUT_MOD, "w") as f:
        json.dump({"timestamp": timestamp, "source": MOD_CONTAINER, "stats": mod_data}, f, indent=2)
    fix_ownership(OUTPUT_MOD)
    print(f"  Mod stats  -> {OUTPUT_MOD}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract DAB stats to JSON")
    parser.add_argument("--loop", type=int, default=0, help="Poll interval in seconds (0 = run once)")
    args = parser.parse_args()
    if args.loop > 0:
        print(f"Polling every {args.loop} seconds. Ctrl+C to stop.")
        try:
            while True:
                collect_and_save()
                time.sleep(args.loop)
        except KeyboardInterrupt:
            print("\nStopped.")
    else:
        collect_and_save()
