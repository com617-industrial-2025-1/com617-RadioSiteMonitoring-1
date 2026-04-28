#!/bin/bash
# start_mode_b.sh  —  Demo day / USRP B200 hardware
# Starts the full DAB software chain in Docker with USRP B200 output.

DAB_DIR="/home/sebastian/Desktop/DAB_project"
COMPOSE="$DAB_DIR/docker-compose.mode_b.yml"

echo "============================================"
echo "  DAB Project  —  Mode B (USRP B200)"
echo "============================================"

# Check Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "ERROR: Docker is not running. Start it with:"
    echo "  sudo systemctl start docker"
    exit 1
fi

# Check USRP B200 is connected
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

# If containers are already up, bring them down cleanly first
if docker ps --format '{{.Names}}' | grep -q "dab_"; then
    echo ">> Existing containers found. Bringing them down first..."
    docker compose -f "$COMPOSE" down
fi

echo ""
echo ">> Starting containers..."
echo "   (Press Ctrl+C to stop)"
echo ""

docker compose -f "$COMPOSE" up
