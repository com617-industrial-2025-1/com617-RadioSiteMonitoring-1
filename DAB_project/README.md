# DAB Project — Docker Setup

## Folder structure

```
DAB_project/
├── docker-compose.mode_a.yml   ← Home / no hardware
├── docker-compose.mode_b.yml   ← Demo day / USRP B200
│
├── encoder/
│   └── Dockerfile              ← Builds odr-audioenc from source
├── mux/
│   └── Dockerfile              ← Builds odr-dabmux (next branch) from source
├── mod/
│   └── Dockerfile              ← Builds odr-dabmod + UHD from source
│
└── configs/
    ├── mode_a/
    │   ├── test.mux            ← Mux config (management port enabled)
    │   └── ports25_mod.ini     ← Mod config (output=file → /dev/null)
    └── mode_b/
        ├── test.mux            ← Same mux config
        └── ports25_mod.ini     ← Mod config (output=uhd → USRP B200)
```

Config files are mounted as volumes — edit them on the host and restart
the relevant container. No rebuild needed for config changes.

---

## Prerequisites

```bash
# Install Docker and the Compose plugin
sudo apt install docker.io docker-compose-plugin

# Allow your user to run Docker without sudo
sudo usermod -aG docker $USER
# Log out and back in for this to take effect
```

---

## Mode A — Home / no hardware

```bash
cd /home/sebastian/Desktop/DAB_project

# First time (or after a Dockerfile change): builds all three images.
# Takes ~10-15 minutes due to building from source.
docker compose -f docker-compose.mode_a.yml up --build

# Subsequent runs (no code changes): skips rebuild, starts in seconds.
docker compose -f docker-compose.mode_a.yml up

# Run in background
docker compose -f docker-compose.mode_a.yml up -d

# Stop everything
docker compose -f docker-compose.mode_a.yml down
```

### Verifying it's working (Mode A)

```bash
# Check all three containers are running
docker ps

# Watch live logs from all containers
docker compose -f docker-compose.mode_a.yml logs -f

# Watch logs from one container only
docker compose -f docker-compose.mode_a.yml logs -f mux

# Query mux stats (management port)
nc 127.0.0.1 12720

# Telnet into mux remote control
telnet 127.0.0.1 12721

# Telnet into mod remote control
telnet 127.0.0.1 2120
```

---

## Mode B — Demo day / USRP B200

```bash
# 1. Plug in the USRP B200 via USB 3.0 (blue port)

# 2. Confirm the host can see it
lsusb | grep Ettus
# Expected output: Bus 00X Device 00X: ID 2500:0020 Ettus Research LLC USRP B200

# 3. Start the stack
cd /home/sebastian/Desktop/DAB_project
docker compose -f docker-compose.mode_b.yml up --build

# 4. Watch the mod container logs to confirm the B200 initialises
docker compose -f docker-compose.mode_b.yml logs -f mod
# Look for lines like:
#   Opening USRP device...
#   Setting TX Rate: 2.048 MSps
#   Setting TX Freq: 194.064 MHz
```

### If the B200 isn't found

```bash
# Check UHD can see the device from the host (outside Docker)
uhd_find_devices

# Check USB permissions
lsusb -v | grep -A5 Ettus

# The mod container runs privileged with /dev/bus/usb mounted, so if
# uhd_find_devices works on the host it will also work in the container.
```

---

## Rebuilding after config changes

Config file changes (.mux or .ini): just restart the affected container —
```bash
docker compose -f docker-compose.mode_a.yml restart mux
docker compose -f docker-compose.mode_a.yml restart mod
```

Dockerfile changes (e.g. different source branch): rebuild that image —
```bash
docker compose -f docker-compose.mode_a.yml build mux
docker compose -f docker-compose.mode_a.yml up
```

---

## OpenNMS monitoring ports (exposed to host on both modes)

| Port | Service | What it gives you |
|------|---------|-------------------|
| 12720 | odr-dabmux management | JSON stats: buffers, overruns, underruns per subchannel |
| 12721 | odr-dabmux telnet RC | Runtime mux parameter inspection |
| 2120  | odr-dabmod telnet RC | Modulator gain, signal stats |
| 9400  | odr-dabmod ZMQ RC | Programmatic mod stats for OpenNMS scripts |

All four are bound to 127.0.0.1 (localhost only) — they are not exposed
to the wider network, which matters if the demo machine is on a uni network.
