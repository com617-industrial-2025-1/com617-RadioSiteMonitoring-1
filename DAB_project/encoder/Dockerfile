FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y software-properties-common \
    && add-apt-repository universe \
    && apt-get update && apt-get install -y \
    git build-essential automake autoconf libtool pkg-config \
    libfdk-aac-dev libzmq3-dev libcurl4-openssl-dev curl \
    vlc libvlc-dev \
    && rm -rf /var/lib/apt/lists/*
RUN git clone --branch next --depth 1 \
    https://github.com/Opendigitalradio/ODR-AudioEnc.git /build/ODR-AudioEnc
WORKDIR /build/ODR-AudioEnc
RUN autoreconf -fi && ./configure --enable-vlc && make -j$(nproc) && make install
WORKDIR /
