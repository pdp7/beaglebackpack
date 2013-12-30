#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight

# source: https://github.com/pdp7/beaglebackpack/blob/master/README.md
# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = EightByEight(address=0x70)
grid2 = EightByEight(address=0x71)

print "Press CTRL+Z to exit"

# Continually update the 8x8 display one pixel at a time
while(True):
  for x in range(0, 8):
    for y in range(0, 8):
      grid.setPixel(x, y)
      grid2.setPixel(x, y)
      time.sleep(0.1)
  time.sleep(0.5)
  grid.clear()
  grid2.clear()
  time.sleep(0.5)
