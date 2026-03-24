#!/bin/bash
# start_mode_b.sh
# Starts the full DAB software chain in Mode B (USRP B200 hardware).
# Written by myself (Sebastian) for use on demo day.
# The modulator transmits IQ samples to the USRP B200 on channel 7D (194.064 MHz).

DAB_DIR="/home/sebastian/Desktop/DAB_project"
COMPOSE="$DAB_DIR/docker-compose.mode_b.yml"

echo "============================================"
echo "  DAB Project  —  Mode B (USRP B200)"
echo "============================================"

# Exit early if the Docker daemon is not running.
if ! docker info > /dev/null 2>&1; then
    echo "ERROR: Docker is not running. Start it with:"
    echo "  sudo systemctl start docker"
    exit 1
fi

# Check the USRP B200 is detected on USB before attempting to start.
# USB vendor:product ID 2500:0020 identifies the Ettus USRP B200.
echo ">> Checking for USRP B200..."
if ! lsusb | grep -q "2500:0020"; then
    echo ""
    echo "ERROR: USRP B200 not detected on USB."
    echo "  - Check the USB 3.0 cable is connected (blue port)"
    echo "  - Try: lsusb | grep Ettus"
    echo ""
    exit 1
fi
echo "   USRP B200 found."

cd "$DAB_DIR"

# If any DAB containers are already running, bring them down cleanly
# before starting fresh to avoid port conflicts.
if docker ps --format '{{.Names}}' | grep -q "dab_"; then
    echo ">> Existing containers found. Bringing them down first..."
    docker compose -f "$COMPOSE" down
fi

echo ""
echo ">> Starting containers..."
echo "   (Press Ctrl+C to stop)"
echo ""

docker compose -f "$COMPOSE" up
