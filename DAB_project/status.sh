#!/bin/bash
# status.sh  —  Shows running containers and tails logs.
# Usage:
#   ./status.sh           — shows which containers are up
#   ./status.sh logs      — tails logs from all containers
#   ./status.sh logs mux  — tails logs from one container (mux/mod/encoder)

DAB_DIR="/home/sebastian/Desktop/DAB_project"

echo "============================================"
echo "  DAB Project  —  Status"
echo "============================================"
echo ""

# Show running containers
echo ">> Containers:"
docker ps --format "  {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep "dab_" || echo "  No DAB containers running."
echo ""

# Show exposed ports
echo ">> Monitoring ports (if running):"
echo "   Mux stats:        nc 127.0.0.1 12720"
echo "   Mux remote ctrl:  telnet 127.0.0.1 12721"
echo "   Mod remote ctrl:  telnet 127.0.0.1 2120"
echo "   Mod ZMQ ctrl:     tcp://127.0.0.1:9400"
echo ""

# Handle log tailing
if [ "$1" = "logs" ]; then
    cd "$DAB_DIR"
    if [ -n "$2" ]; then
        echo ">> Tailing logs for: $2"
        echo "   (Ctrl+C to exit)"
        echo ""
        if docker inspect dab_mod 2>/dev/null | grep -q "mode_b"; then
            docker compose -f docker-compose.mode_b.yml logs -f "$2"
        else
            docker compose -f docker-compose.mode_a.yml logs -f "$2"
        fi
    else
        echo ">> Tailing logs for all containers:"
        echo "   (Ctrl+C to exit)"
        echo ""
        if docker inspect dab_mod 2>/dev/null | grep -q "mode_b"; then
            docker compose -f docker-compose.mode_b.yml logs -f
        else
            docker compose -f docker-compose.mode_a.yml logs -f
        fi
    fi
fi
