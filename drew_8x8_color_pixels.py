#!/usr/bin/python

import Adafruit_BBIO.ADC as ADC
import random
import time
import datetime
from Adafruit_8x8 import ColorEightByEight

ADC.setup()

grid = ColorEightByEight(address=0x70)
matrix = [ [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0] ]

for x in range(0, 8):
   for y in range(0, 8):
       grid.setPixel(x, y, 0)
 
# Continually update the 8x8 display one pixel at a time
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
