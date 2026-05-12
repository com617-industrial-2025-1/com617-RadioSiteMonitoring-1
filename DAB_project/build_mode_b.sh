#!/bin/bash
echo "Building Mode B (USRP live RF)..."
docker compose -f docker-compose.yml -f docker-compose_mode_b.yml build
