#!/usr/bin/env sh

# Bombardier installation
sudo apt-get update
wget https://github.com/codesenberg/bombardier/releases/download/v1.2.6/bombardier-linux-amd64

sudo mv bombardier-linux-amd64 /usr/local/bin/bombardier
sudo chmod +x /usr/local/bin/bombardier
rm -rf bombardier-linux-amd64
