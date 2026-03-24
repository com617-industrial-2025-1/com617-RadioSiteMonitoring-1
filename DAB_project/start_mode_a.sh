#!/bin/bash
# start_mode_a.sh
# Starts the full DAB software chain in Mode A (no hardware).
# Written by myself (Sebastian) for use when developing at home.
# The modulator runs the full pipeline but discards output to /dev/null.

DAB_DIR="/home/sebastian/Desktop/DAB_project"
COMPOSE="$DAB_DIR/docker-compose.mode_a.yml"

echo "============================================"
echo "  DAB Project  —  Mode A (no hardware)"
echo "============================================"

# Exit early if the Docker daemon is not running.
if ! docker info > /dev/null 2>&1; then
    echo "ERROR: Docker is not running. Start it with:"
    echo "  sudo systemctl start docker"
    exit 1
fi

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
