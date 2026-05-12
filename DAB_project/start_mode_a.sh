#!/bin/bash
echo "Starting Mode A (software only)..."
docker compose -f docker-compose.yml -f docker-compose_mode_a.yml up -d
