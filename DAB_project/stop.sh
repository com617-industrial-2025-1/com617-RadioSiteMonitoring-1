#!/bin/bash
# stop.sh
# Stops whichever DAB mode is currently running.
# Detects whether Mode A or Mode B is active by inspecting the mod container config.

DAB_DIR="/home/sebastian/Desktop/DAB_project"

echo "============================================"
echo "  DAB Project  —  Stopping"
echo "============================================"

cd "$DAB_DIR"

# Check if any DAB containers are running before attempting to stop.
if docker ps --format '{{.Names}}' | grep -q "dab_"; then
    # Inspect the mod container to determine which mode is active.
    if docker inspect dab_mod 2>/dev/null | grep -q "mode_b"; then
        echo ">> Stopping Mode B (USRP B200)..."
        docker compose -f docker-compose.mode_b.yml down
    else
        echo ">> Stopping Mode A (no hardware)..."
        docker compose -f docker-compose.mode_a.yml down
    fi
    echo ">> All containers stopped."
else
    echo ">> No DAB containers are currently running."
fi
