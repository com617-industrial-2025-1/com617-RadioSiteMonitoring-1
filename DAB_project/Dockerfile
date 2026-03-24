FROM ubuntu:22.04

# Suppress interactive prompts during package installation.
ENV DEBIAN_FRONTEND=noninteractive

# Install build tools and libraries needed to compile ODR-AudioEnc.
# libfdk-aac-dev provides the AAC encoder used for DAB+ audio.
# libvlc-dev enables VLC input so the encoder can read internet radio streams.
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    automake \
    autoconf \
    libtool \
    pkg-config \
    libfdk-aac-dev \
    libzmq3-dev \
    libcurl4-openssl-dev \
    curl \
    vlc \
    libvlc-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone the next branch of ODR-AudioEnc.
# The next branch is used to match the mux and mod versions.
RUN git clone --branch next --depth 1 \
    https://github.com/Opendigitalradio/ODR-AudioEnc.git /build/ODR-AudioEnc

WORKDIR /build/ODR-AudioEnc

# autoreconf generates the build system files that are not stored in the repo.
# --enable-vlc enables VLC input support for reading internet radio streams.
RUN autoreconf -fi && \
    ./configure --enable-vlc && \
    make -j$(nproc) && \
    make install

WORKDIR /
