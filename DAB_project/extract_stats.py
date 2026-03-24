#!/usr/bin/env python3
# extract_stats.py
# Written by myself (Sebastian) as part of the DAB radio monitoring project.
#
# Queries both the mux and mod containers and saves their stats as JSON files.
# The mux is queried via docker exec using ZMQ inside the container, because
# the ZMQ stats socket only binds to localhost inside Docker and cannot be
# reached directly from the host.
# The mod is queried via its telnet remote control interface on port 2120.
#
# Output files:
#   stats_mux.json  —  subchannel buffer levels, underruns, overruns, stream state
#   stats_mod.json  —  ensemble info, gain settings, EDI source, modulator uptime
#
# Usage:
#   sudo python3 extract_stats.py              # run once
#   sudo python3 extract_stats.py --loop 10   # poll every 10 seconds

import json
import time
import os
import pwd
import argparse
import subprocess
from datetime import datetime, timezone

# Names of the Docker containers to query.
MUX_CONTAINER = "dab_mux"
MOD_CONTAINER = "dab_mod"

# Output file paths — written to the current working directory.
OUTPUT_MUX = "stats_mux.json"
OUTPUT_MOD = "stats_mod.json"

# Detect the real user who invoked sudo so output files are not owned by root.
# SUDO_USER is set automatically by sudo. Falls back to USER if not using sudo.
REAL_USER = os.environ.get("SUDO_USER", os.environ.get("USER", "sebastian"))

# Python code run inside the mux container via docker exec.
# Connects to the ZMQ stats server on port 12720 and retrieves:
#   - info: service name and version
#   - values: per-subchannel input buffer stats
#   - output_values: number of active EDI TCP connections
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

# Python code run inside the mod container via docker exec.
# Connects to the telnet remote control on port 2120 and queries
# key modulator parameters. The RC prompt adds a trailing ">" to
# each response which is stripped before saving.
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
    """Run a Python query inside a container and return the parsed JSON output."""
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
    """Reset file ownership to the real user after writing with sudo.
    Without this, output files would be owned by root and unreadable."""
    try:
        uid = pwd.getpwnam(REAL_USER).pw_uid
        gid = pwd.getpwnam(REAL_USER).pw_gid
        os.chown(filepath, uid, gid)
    except Exception:
        pass


def collect_and_save():
    """Query both containers and write stats to JSON files."""
    timestamp = datetime.now(timezone.utc).isoformat()
    print(f"[{timestamp}] Collecting stats...")

    # Query mux and save to file.
    mux_data = docker_exec(MUX_CONTAINER, MUX_QUERY)
    with open(OUTPUT_MUX, "w") as f:
        json.dump({"timestamp": timestamp, "source": MUX_CONTAINER, "stats": mux_data}, f, indent=2)
    fix_ownership(OUTPUT_MUX)
    print(f"  Mux stats  -> {OUTPUT_MUX}")

    # Query mod and save to file.
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
        # Run in a loop, polling at the specified interval until Ctrl+C.
        print(f"Polling every {args.loop} seconds. Ctrl+C to stop.")
        try:
            while True:
                collect_and_save()
                time.sleep(args.loop)
        except KeyboardInterrupt:
            print("\nStopped.")
    else:
        collect_and_save()
