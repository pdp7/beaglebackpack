#!/usr/bin/python
# AUTHOR: Drew Fustini
# DESC: BeagleBone Black demo: Plot ADC samples on Adafruit 8x8 Bi-Color LED Matrix
# README: https://github.com/pdp7/beaglebackpack/blob/master/README.md
# LICENSE: Creative Commons CC0 http://creativecommons.org/choose/zero/

# refer to https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/
from Adafruit_8x8 import ColorEightByEight
# refer to https://github.com/adafruit/PyBBIO
import Adafruit_BBIO.ADC as ADC
import random
import time
import datetime

# Enable debug output
DEBUG = True

# display buffer to represent the 8x8 LED matrix
matrix = [ [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0] ]

grid = ColorEightByEight(address=0x70)

# clear matrix
for x in range(0, 8):
   for y in range(0, 8):
       grid.setPixel(x, y, 0)
 
ADC.setup()

# continually scroll the matrix and plot new ADC sample
while(True):
 
   for x in range(7):
       for y in range(8):
           matrix[x][y] = matrix[x+1][y]
  
   # read sample from ADC and convert to integer  0-8
   adc_sample = ADC.read("P9_40")
   sample_flot = adc_sample*8.0
   if sample_flot > 7.5:
       sample_flot = 8
   sample = int(sample_flot)
   if DEBUG:
       print "adc_sample=", adc_sample, "sample_flot=", sample_flot, "sample=", sample

   # clear column
   for i in range(8):
       matrix[7][i] = 0

   # plot sample on right most column
   for i in range(sample):
       color = 0
       if (i >= 0 and i <= 3):
           color = 1 #GREEN
       elif (i > 3 and i <= 6): 
           color = 3 #ORANGE/YELLOW
       elif (i > 6 and i < 8): 
           color = 2 #RED
       matrix[7][i] = color
    
   # write contents of matrix to the physical display
   for row in matrix:
       for x in range(8):
           for y in range(8):
               if(matrix[x][y]>0):
                   grid.setPixel(y, x, matrix[x][y])
               else:
                   grid.setPixel(y, x, 0)
