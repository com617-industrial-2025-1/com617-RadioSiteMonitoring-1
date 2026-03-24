#!/bin/bash
# status.sh
# Shows the status of all DAB containers and optionally tails their logs.
#
# Usage:
#   ./status.sh                — show which containers are up
#   ./status.sh logs           — tail logs from all containers
#   ./status.sh logs mux       — tail logs from the mux container only
#   ./status.sh logs mod       — tail logs from the mod container only
#   ./status.sh logs encoder   — tail logs from the encoder container only

DAB_DIR="/home/sebastian/Desktop/DAB_project"

echo "============================================"
echo "  DAB Project  —  Status"
echo "============================================"
echo ""

# List all running DAB containers with their status and exposed ports.
echo ">> Containers:"
docker ps --format "  {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep "dab_" || echo "  No DAB containers running."
echo ""

# Print the monitoring ports for quick reference.
echo ">> Monitoring ports (if running):"
echo "   Mux stats:        nc 127.0.0.1 12720"
echo "   Mux remote ctrl:  telnet 127.0.0.1 12721"
echo "   Mod remote ctrl:  telnet 127.0.0.1 2120"
echo "   Mod ZMQ ctrl:     tcp://127.0.0.1:9400"
echo ""

# If "logs" is passed as the first argument, tail the container logs.
if [ "$1" = "logs" ]; then
    cd "$DAB_DIR"
    # Detect which compose file is active.
    if docker inspect dab_mod 2>/dev/null | grep -q "mode_b"; then
        COMPOSE="docker-compose.mode_b.yml"
    else
        COMPOSE="docker-compose.mode_a.yml"
    fi

    if [ -n "$2" ]; then
        # Tail logs for a specific container if a name was given.
        echo ">> Tailing logs for: $2"
        echo "   (Ctrl+C to exit)"
        echo ""
        docker compose -f "$COMPOSE" logs -f "$2"
    else
        # Tail logs for all containers.
        echo ">> Tailing logs for all containers:"
        echo "   (Ctrl+C to exit)"
        echo ""
        docker compose -f "$COMPOSE" logs -f
    fi
fi
