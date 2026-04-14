#!/bin/bash
# stop.sh  —  Stops whichever mode is currently running.

DAB_DIR="/home/sebastian/Desktop/DAB_project"

echo "============================================"
echo "  DAB Project  —  Stopping"
echo "============================================"

cd "$DAB_DIR"

# Detect which compose file is active and bring it down
if docker ps --format '{{.Names}}' | grep -q "dab_"; then
    # Check which mode is running by looking at the mod container config
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
