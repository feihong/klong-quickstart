# Feihong's Klong Quickstart

## Installation

Install normal Klong

    wget https://t3x.org/klong/klong20221212.tgz -O klong.tgz
    tar xvf klong.tgz
    cd klong
    make
    cp kg /usr/local/bin

Set `KLONGPATH` environment variable to `./klong/lib` directory.

Install Python, then install KlongPy
 
    pip install --requirement requirements.txt

Install the KlongPy Jupyter kernel

    git clone --depth 1 https://github.com/briangu/klupyter
    cd klupyter
    pip install .
    jupyter kernelspec install --user klongpy_kernel
    cd ..
    rm -rf klupyter

## Commands

Start Klong REPL

    make kg

Start KlongPy REPL

    make py

Upgrade KlongPy

    make upgrade

## Links

- [KlongPy](https://github.com/briangu/klongpy)
- [Klong Reference Manual](https://t3x.org/klong/klong-ref.txt.html)
