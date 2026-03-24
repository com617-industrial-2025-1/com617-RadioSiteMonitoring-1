FROM ubuntu:22.04

# Suppress interactive prompts during package installation.
ENV DEBIAN_FRONTEND=noninteractive

# Install build tools and libraries needed to compile ODR-DabMux.
# libzmq3-dev provides the ZMQ stats server used by extract_stats.py.
# python3-zmq is needed to run the bundled stats scripts inside the container.
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    automake \
    autoconf \
    libtool \
    pkg-config \
    libzmq3-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libcurl4-openssl-dev \
    python3 \
    python3-zmq \
    && rm -rf /var/lib/apt/lists/*

# Clone the next branch of ODR-DabMux.
# The next branch includes the ZMQ management stats server
# and JSON stats output used by extract_stats.py.
RUN git clone --branch next --depth 1 \
    https://github.com/Opendigitalradio/ODR-DabMux.git /build/ODR-DabMux

WORKDIR /build/ODR-DabMux

# autoreconf generates the build system files that are not stored in the repo.
RUN autoreconf -fi && \
    ./configure && \
    make -j$(nproc) && \
    make install

# The .mux config file is mounted as a Docker volume at runtime.
# This means config changes on the host take effect with a container
# restart and do not require a full image rebuild.
WORKDIR /
