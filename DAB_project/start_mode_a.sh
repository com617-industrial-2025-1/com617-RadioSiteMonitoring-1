#!/bin/bash
# start_mode_a.sh  —  Home / no hardware
# Starts the full DAB software chain in Docker (no USRP required).

DAB_DIR="/home/sebastian/Desktop/DAB_project"
COMPOSE="$DAB_DIR/docker-compose.mode_a.yml"

echo "============================================"
echo "  DAB Project  —  Mode A (no hardware)"
echo "============================================"

# Check Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "ERROR: Docker is not running. Start it with:"
    echo "  sudo systemctl start docker"
    exit 1
fi

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
