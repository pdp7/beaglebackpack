#!/bin/sh

# readme: https://github.com/pdp7/beaglebackpack/blob/master/README.md

# Set LEDBACKPATH_PATH to where is Adafruit_LEDBackpack locate on your system
LEDBACKPATH_PATH=$HOME/Adafruit-Raspberry-Pi-Python-Code/Adafruit_LEDBackpack

export PYTHONPATH=$PATH:${LEDBACKPATH_PATH}
python plot.py $@
