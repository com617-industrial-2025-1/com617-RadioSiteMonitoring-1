FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    git build-essential automake autoconf libtool pkg-config \
    libzmq3-dev libboost-system-dev libboost-thread-dev \
    libuhd-dev uhd-host python3 python3-mako \
    && rm -rf /var/lib/apt/lists/*
RUN uhd_images_downloader -t b2xx
RUN git clone --branch next --depth 1 \
    https://github.com/Opendigitalradio/ODR-DabMod.git /build/ODR-DabMod
WORKDIR /build/ODR-DabMod
RUN autoreconf -fi && ./configure --enable-output-uhd && make -j$(nproc) && make install
WORKDIR /
