#!/bin/bash
echo "Starting Mode B (USRP live RF)..."
docker compose -f docker-compose.yml -f docker-compose_mode_b.yml up -d
