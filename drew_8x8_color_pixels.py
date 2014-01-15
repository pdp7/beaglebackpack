#!/usr/bin/python

import Adafruit_BBIO.ADC as ADC
import random
import time
import datetime
from Adafruit_8x8 import ColorEightByEight

ADC.setup()

grid = ColorEightByEight(address=0x70)
matrix = [ [1,1,1,1,1,0,0,0],
           [1,1,0,0,0,0,0,0],
           [1,1,1,1,0,0,0,0],
           [1,1,1,1,1,1,1,0],
           [1,1,1,1,1,0,0,0],
           [1,1,1,1,1,1,0,0],
           [1,1,1,1,1,1,1,0],
           [1,1,1,1,1,0,0,0] ]

for row in matrix:
    print row

#print "================================="

samples = [1,2,3,4,5,6,7,8, 8,7,6,5,4,3,2,1, 8,1,8,1,8,1,8,1]

iter = 0

for x in range(0, 8):
   for y in range(0, 8):
       grid.setPixel(x, y, 0)
 

# Continually update the 8x8 display one pixel at a time
iter += 1
while(True):
 
   #startMillis=0 #millis();  # Start of sample window
   #peakToPeak = 0  #peak-to-peak level
 
   #signalMax = 0
   #signalMin = 1024
 
   #while (millis() - startMillis < sampleWindow)
      #sample = analogRead(0); 
      #if (sample < 1024)  // toss out spurious readings
         #if (sample > signalMax)
            #signalMax = sample;  // save just the max levels
         #else if (sample < signalMin)
            #signalMin = sample;  // save just the min levels
   #peakToPeak = signalMax - signalMin;
 
   # map 1v p-p level to the max scale of the display
   #displayPeak = map(peakToPeak, 0, 1023, 0, maxScale);
 
   # Update the display:
   #for (int i = 0; i < 7; i++)  # shift the display left
   #   matrix.displaybuffer[i] = matrix.displaybuffer[i+1];
 
   #for row in matrix:
   #   for i in range(len(row)-1):
   #       row[i] = row[i+1]
   for x in range(7):
       for y in range(8):
           matrix[x][y] = matrix[x+1][y]
   #sample = random.randint(1,8) 
   adc_sample = ADC.read("P9_40")
   print "adc_sample=", adc_sample
   sample_flot = adc_sample*8.0
   print "sample_flot=", sample_flot
   if sample_flot > 7.5:
       sample_flot = 8
   sample = int(sample_flot)
   print "sample=", sample
   for i in range(8):
       #nprint "i=", i
       matrix[7][i] = 0
   for i in range(sample):
       #print "i=", i
       matrix[7][i] = 1

   # set the new sample
   for a in range(0, len(samples)/8):
       for sample in samples[a*8:((a*8)+8)]:
           for i in range(0,8):
               if (i >= sample): 
                   color = 0
               elif (i > 5 and i <= 7): 
                   color = 2
               elif (i > 3 and i <= 5): 
                   color = 3
               elif (i >= 0 and i <= 3):
                   color = 1
               #print "a=", a, " a*8=", a*8, "(a*8)+8=", (a*8)+8, " i=", i, " sample=", sample, " color=", color
               #matrix[i][7] = color
     
   for row in matrix:
       #print "row: ", row
       for x in range(8):
           for y in range(8):
               #print "matrix[", x, ",", y, "]=", matrix[x][y]
               if(matrix[x][y]==1):
                   grid.setPixel(y, x, 1)
               else:
                   grid.setPixel(y, x, 0)
      

   #print "============"
   ##time.sleep(0.1)


