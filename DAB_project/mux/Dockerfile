FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    git build-essential automake autoconf libtool pkg-config \
    libzmq3-dev libboost-system-dev libboost-thread-dev \
    libcurl4-openssl-dev python3 python3-zmq \
    && rm -rf /var/lib/apt/lists/*
RUN git clone --branch next --depth 1 \
    https://github.com/Opendigitalradio/ODR-DabMux.git /build/ODR-DabMux
WORKDIR /build/ODR-DabMux
RUN autoreconf -fi && ./configure && make -j$(nproc) && make install
WORKDIR /
