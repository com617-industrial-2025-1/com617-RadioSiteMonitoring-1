FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y software-properties-common \
    && add-apt-repository universe \
    && apt-get update && apt-get install -y \
    git build-essential automake autoconf libtool pkg-config \
    libzmq3-dev libboost-system-dev libboost-thread-dev \
    libuhd-dev uhd-host python3 python3-mako \
    && rm -rf /var/lib/apt/lists/*
RUN uhd_images_downloader -t b2xx
RUN git clone --branch next --depth 1 \
    https://github.com/Opendigitalradio/ODR-DabMod.git /build/ODR-DabMod
WORKDIR /build/ODR-DabMod
# Patch remote control to bind on all interfaces instead of localhost only
RUN sed -i 's|m_socket.listen(m_port, "localhost")|m_socket.listen(m_port, "0.0.0.0")|g' lib/RemoteControl.cpp
RUN autoreconf -fi && ./configure --enable-output-uhd && make -j$(nproc) && make install
WORKDIR /
