#!/bin/bash
echo "Building Mode A (software only)..."
docker compose -f docker-compose.yml -f docker-compose_mode_a.yml build
