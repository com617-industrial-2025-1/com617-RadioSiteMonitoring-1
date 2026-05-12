# OpenNMS for DAB Project

Minimal OpenNMS Horizon + PostgreSQL stack, joined to `dab_net` so it can
poll the `dab_collector` SNMP agent directly.

## Directory layout

```
opennms-dab/
├── docker-compose.yml
└── container-fs/
    └── horizon/
        ├── etc/
        │   └── conf.d/
        │       └── confd.toml              # points horizon at the overlay config
        └── opt/
            └── opennms-overlay/
                ├── confd/
                │   └── horizon-config.yaml # DB credentials + RRD strategy
                └── etc/
                    ├── snmp-config.xml     # SNMP community / target config
                    ├── datacollection-config.xml  # which MIB groups to collect
                    └── datacollection/
                        └── ODR-DAB-MIB.xml         ← TO BE ADDED
```

## Still needed (waiting on MIB work)

| File | Purpose |
|------|---------|
| `etc/datacollection/ODR-DAB-MIB.xml` | Tells OpenNMS which OIDs to poll and how to store them |
| `etc/snmp-graph.properties.d/ODR-DAB-MIB-graph.properties` | RRD graph definitions for the web UI |
| `etc/events/ODR-DAB-MIB.events.xml` | (Optional) threshold alerts for underruns, restarts etc. |

## Usage

```bash
# First time - OpenNMS initialises its DB schema on startup (takes ~2 min)
docker compose up -d

# Watch startup
docker compose logs -f horizon

# Web UI
http://localhost:8980/opennms   (admin / admin)

# Once ODR-DAB-MIB.xml is in place, add the collector node via the web UI:
# Admin → Provisioning Requisitions → add node with IP = dab_collector
# or use the REST API / requisition XML in etc/imports/
```

## Pre-requisites

- `dab_net` Docker network must already exist (created by the DAB `docker compose up`)
- The `dab_collector` container must be running with snmpd on UDP 161

