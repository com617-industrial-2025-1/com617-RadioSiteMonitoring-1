# DAB_project — ODR-mmbTools Containerised DAB Stack

A containerised Digital Audio Broadcasting (DAB) stack built on ODR-mmbTools,
with integrated SNMP monitoring via a dedicated collector container.
Supports two operating modes: software-only (Mode A) and live RF output via
USRP B200 SDR (Mode B).

---

## Project Structure

```
DAB_project/
├── docker-compose.yml              # Base stack definition (all services)
├── docker-compose_mode_a.yml       # Mode A overlay — software only (/dev/null output)
├── docker-compose_mode_b.yml       # Mode B overlay — USRP B200 live RF output
│
├── encoder/
│   └── Dockerfile                  # ODR-AudioEnc (VLC input, DAB+ encoder)
├── mux/
│   └── Dockerfile                  # ODR-DabMux (multiplexer)
├── mod/
│   └── Dockerfile                  # ODR-DabMod (modulator, UHD support)
├── collector/
│   ├── Dockerfile                  # Ubuntu 24.04 + snmpd + Python
│   ├── snmpd.conf                  # SNMP agent config, pass_persist registration
│   ├── pass_persist.py             # SNMP pass_persist bridge (ZMQ + Telnet → OID tree)
│   └── debug.py                    # Live human-readable stats viewer
│
└── configs/
    ├── mode_a/
    │   ├── test.mux                # Mux config — Mode A (ensemble: Solent Uni)
    │   └── ports25_mod.ini         # Mod config — file output to /dev/null
    └── mode_b/
        ├── test.mux                # Mux config — Mode B (ensemble: Solent Demo)
        └── ports25_mod.ini         # Mod config — USRP B200, 229.072 MHz (Ch 12D)
```

---

## Containers

| Container      | Image          | Role                                        |
|----------------|----------------|---------------------------------------------|
| `dab_encoder`  | encoder        | Encodes 3 live internet radio streams to DAB+ EDI |
| `dab_mux`      | mux            | Multiplexes subchannels into a DAB ensemble |
| `dab_mod`      | mod            | Modulates and outputs DAB signal            |
| `dab_collector`| collector      | SNMP agent — polls mux/mod, exposes metrics |

All containers communicate over the internal Docker bridge network `dab_net`.

---

## Modes

| | Mode A | Mode B |
|---|---|---|
| **Purpose** | Development / testing — no hardware needed | Live RF broadcast |
| **Modulator output** | `/dev/null` (discarded) | USRP B200 SDR |
| **Frequency** | N/A | 229.072 MHz (DAB Channel 12D) |
| **Ensemble label** | Solent Uni | Solent Demo |
| **USB device passthrough** | Not required | Required (`/dev/bus/usb`) |

---

## Building the Stack

> Run all commands from the project root directory.

### Mode A — Software Only

```bash
docker compose -f docker-compose.yml -f docker-compose_mode_a.yml build
```

### Mode B — USRP Live RF

```bash
docker compose -f docker-compose.yml -f docker-compose_mode_b.yml build
```

> **Note:** The modulator image takes the longest to build — it compiles
> ODR-DabMod with UHD support and downloads USRP firmware images.
> Allow 10–20 minutes on first build.

---

## Starting the Stack

### Mode A

```bash
docker compose -f docker-compose.yml -f docker-compose_mode_a.yml up -d
```

### Mode B

```bash
docker compose -f docker-compose.yml -f docker-compose_mode_b.yml up -d
```

### Verify all containers are running

```bash
docker ps
```

Expected output — four containers should be listed with status `Up`:

```
CONTAINER ID   IMAGE         NAMES           STATUS
xxxxxxxxxxxx   mod           dab_mod         Up 2 minutes
xxxxxxxxxxxx   mux           dab_mux         Up 2 minutes
xxxxxxxxxxxx   encoder       dab_encoder     Up 2 minutes
xxxxxxxxxxxx   collector     dab_collector   Up 2 minutes
```

---

## Stopping the Stack

### Mode A

```bash
docker compose -f docker-compose.yml -f docker-compose_mode_a.yml down
```

### Mode B

```bash
docker compose -f docker-compose.yml -f docker-compose_mode_b.yml down
```

---

## Using debug.py — Live Stats Viewer

`debug.py` runs inside the collector container and gives a human-readable
live view of mux buffer stats, subchannel states, and modulator health.

### Single snapshot

```bash
docker exec -it dab_collector python3 /collector/debug.py
```

### Live refresh (every 5 seconds)

```bash
docker exec -it dab_collector python3 /collector/debug.py --loop 5
```

### Compact one-liner mode (useful for logging)

```bash
docker exec -it dab_collector python3 /collector/debug.py --loop 5 --compact
```

### What to look for

| Field | Healthy value |
|---|---|
| Subchannel state | `running` |
| Buffer fill | Above prebuffering threshold (20 for sub-01/02, 40 for sub-03) |
| Underruns / Overruns | `0` |
| Mod restarts | `0` |
| Last EDI decoded | Recent timestamp |

---

## Viewing Container Logs

```bash
# Multiplexer
docker logs dab_mux

# Modulator
docker logs dab_mod

# Encoder
docker logs dab_encoder

# Collector (snmpd)
docker logs dab_collector
```

Follow logs in real time:

```bash
docker logs -f dab_mux
```

---

## Finding the Collector's IP Address (for OpenNMS)

The collector container exposes SNMP on UDP port 161 within `dab_net`.
To add it as a monitored node in OpenNMS, find its IP on the Docker network:

```bash
docker inspect dab_collector \
  --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
```

This returns the container's IP on `dab_net`, e.g. `172.18.0.5`.
Use this IP when adding the node in OpenNMS.

Alternatively, list all container IPs at once:

```bash
docker network inspect dab_net \
  --format '{{range .Containers}}{{.Name}}: {{.IPv4Address}}{{end}}'
```

> **Note:** Container IPs are assigned dynamically and may change if the
> stack is recreated. For a stable address, you can assign a static IP
> in `docker-compose.yml` under the service's `networks:` section.

---

## OpenNMS Integration

### Accessing the OpenNMS Web UI

OpenNMS runs on the host machine. Open a browser and navigate to:

```
http://<host-ip>:8980/opennms
```

Default credentials (change after first login):

```
Username: admin
Password: admin
```

### Adding the Collector as a Monitored Node

1. In the OpenNMS web UI, go to **Info → Add Node** (or **Provisioning → Requisitions**).
2. Enter the collector container's IP address (found above).
3. Set the SNMP community string to `public` (as configured in `snmpd.conf`).
4. Set SNMP version to **v2c**.
5. Click **Add** / **Save** and trigger a scan.

### Verifying SNMP Connectivity

Before adding to OpenNMS, you can test SNMP from the host:

```bash
# Walk the standard system OID
snmpwalk -v2c -c public <collector-ip> 1.3.6.1.2.1.1

# Walk the full DAB custom OID subtree
snmpwalk -v2c -c public <collector-ip> .1.3.6.1.4.1.8072.1.3.2.99

# Poll a specific value — e.g. subchannel 1 state (string)
snmpget -v2c -c public <collector-ip> .1.3.6.1.4.1.8072.1.3.2.99.1.1.7
```

### Custom SNMP OID Tree

All DAB stats are exposed under:

```
.1.3.6.1.4.1.8072.1.3.2.99
```

| Branch | Description |
|---|---|
| `.99.1.1.x` | Subchannel 1 (Radio Caroline) stats |
| `.99.1.2.x` | Subchannel 2 (Flash On Air) stats |
| `.99.1.3.x` | Subchannel 3 (XRadio) stats |
| `.99.2.x` | Mux output connection counts |
| `.99.3.x` | Modulator stats (restarts, EDI, gain, sample rate) |

Per-subchannel leaf OIDs (`.x` suffix):

| OID suffix | Metric |
|---|---|
| `.1` | Buffer max fill |
| `.2` | Buffer min fill |
| `.3` | Underrun count |
| `.4` | Overrun count |
| `.5` | Peak level Left (dBfs × 100) |
| `.6` | Peak level Right (dBfs × 100) |
| `.7` | State string (`running`, `prebuffering`, etc.) |
| `.8` | Uptime (seconds) |

---

## Ports Reference

| Port | Protocol | Exposed to | Purpose |
|---|---|---|---|
| `10001–10003` | TCP | Internal (`dab_net`) | EDI audio input to mux (per subchannel) |
| `12720` | TCP | `127.0.0.1` | Mux ZMQ management port |
| `12721` | TCP | `127.0.0.1` | Mux Telnet remote control |
| `13000` | TCP | Internal (`dab_net`) | EDI output from mux to modulator |
| `2120` | TCP | `127.0.0.1` | Modulator Telnet remote control |
| `9400` | TCP | `127.0.0.1` | Modulator ZMQ control |
| `161` | UDP | `dab_net` | SNMP (collector → OpenNMS) |

---

## Troubleshooting

**Encoder subchannels stuck in `prebuffering`**
Stream sources may be unreachable. Check network connectivity from the encoder container:
```bash
docker exec -it dab_encoder curl -I http://sc6.radiocaroline.net:8040
```

**Modulator not starting (Mode B)**
Ensure the USRP B200 is connected via USB before starting the stack. Verify it is detected:
```bash
uhd_find_devices
```

**SNMP walk returns nothing**
Give the collector ~30 seconds after startup for the background collectors to
populate the cache, then retry.

**Container IP changed after restart**
Recreating the stack reassigns IPs. Re-run the `docker inspect` command and
update the OpenNMS node IP accordingly.
