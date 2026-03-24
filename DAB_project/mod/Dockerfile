FROM ubuntu:22.04

# Suppress interactive prompts during package installation.
ENV DEBIAN_FRONTEND=noninteractive

# Install build tools and libraries needed to compile ODR-DabMod.
# libuhd-dev and uhd-host provide the USRP Hardware Driver for the B200.
# python3-mako is required by the UHD build system.
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
    libuhd-dev \
    uhd-host \
    python3 \
    python3-mako \
    && rm -rf /var/lib/apt/lists/*

# Download the USRP B200 FPGA and firmware images at build time.
# Doing this during the build means demo day does not require an
# internet connection to load the hardware firmware.
RUN uhd_images_downloader -t b2xx

# Clone the next branch of ODR-DabMod.
RUN git clone --branch next --depth 1 \
    https://github.com/Opendigitalradio/ODR-DabMod.git /build/ODR-DabMod

WORKDIR /build/ODR-DabMod

# autoreconf generates the build system files that are not stored in the repo.
# --enable-output-uhd enables USRP B200 hardware output support.
RUN autoreconf -fi && \
    ./configure --enable-output-uhd && \
    make -j$(nproc) && \
    make install

# The .ini config file is mounted as a Docker volume at runtime.
# This means config changes on the host take effect with a container
# restart and do not require a full image rebuild.
WORKDIR /
