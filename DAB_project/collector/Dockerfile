FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    snmpd \
    python3 \
    python3-zmq \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /collector
COPY snmpd.conf /etc/snmp/snmpd.conf
COPY pass_persist.py /collector/pass_persist.py
COPY debug.py /collector/debug.py

RUN chmod +x /collector/pass_persist.py /collector/debug.py

# snmpd runs in foreground; pass_persist is spawned by snmpd
CMD ["snmpd", "-f", "-Lo", "-C", "-c", "/etc/snmp/snmpd.conf"]
