#!/bin/bash
echo "Stopping all containers..."
docker compose -f docker-compose.yml -f docker-compose_mode_a.yml down 2>/dev/null
docker compose -f docker-compose.yml -f docker-compose_mode_b.yml down 2>/dev/null
echo "Done!"
