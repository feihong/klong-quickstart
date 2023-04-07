# Feihong's Klong Quickstart

## Installation

Install normal Klong

    wget https://t3x.org/klong/klong20221212.tgz -O klong.tgz
    tar xvf klong.tgz
    cd klong
    make

Add to your `.zshrc`

    alias kg='rlwrap --always-readline ~/work/klong-quickstart/klong/kg'
    KLONGPATH=~/work/klong-quickstart/klong/lib

Install Python, then install KlongPy
 
    pip install --requirement requirements.txt

Or install KlongPy by downloading its repo

    git clone --depth 1 https://github.com/briangu/klongpy
    cd klongpy
    pip install --editable .

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

Load program from file

    kg -l hanzi.kg

## Links

- [KlongPy](https://github.com/briangu/klongpy)
- [Klong Reference Manual](https://t3x.org/klong/klong-ref.txt.html)
