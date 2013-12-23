'''
Created on Sep 10, 2013
@author: matthassel
Example:
'''
from time import sleep
import numpy as np
from myalphabet import *
from copy import copy
from Adafruit_8x8 import EightByEight
class Text2LED():
     
    def __init__(self):
        pass
    def map_string_to_matrix(self, string):
        '''takes a string, converts it to uppercase, and 
        returns the matching matrix variable if a letter match
        is made.
         
        USAGE:
        mapStringToMatrix("teststring")
        '''
        string = string.upper()
        matrixOfText = []
        for letter in string:
	    matrixOfText.append(myalphabet[letter])
        return matrixOfText
     
    def get_column(self, matrix, i):
	column = []
	for row in matrix:
	     column.append(row[i])
        '''returns a single column from a matrix'''
	return column
     
    def matrix_to_column_list(self, text):
        text2tick = {}
        start = 0
        for z in range(len(text)):
            for c in range(0,8):
                try:
                    col = self.get_column(text[z], c)
                    text2tick[start] = col
                    start += 1
                except IndexError:
                    break
        return text2tick    
     
    def add_to_ticker(self, string, color="green"):
        ticker = []
        text2tick = self.matrix_to_column_list(self.map_string_to_matrix(string))
	total = 0
	for i in text2tick.keys():
	    display = []
	    total = 0
	    for n in range(0, 8):
		if(text2tick[i][n] == 1):
                    total = total + (2**n)
            display.append(total)
            ticker = ticker + display
        return ticker


class LED_TICKER():
         
    def __init__(self):
        self.grid1 = EightByEight(address=0x71)
        self.grid2 = EightByEight(address=0x70)
        self.ticker = []
        self.buffer = []
        self.display = []
         
    def scrolling_ticker_text(self):
        for i in self.ticker:
            self.display = []
            self.display.append(i)
            self.buffer = self.display + self.buffer
            self.update_ticker_w_buffer()
            sleep(0.05)
             
    def update_ticker_w_buffer(self):
	n = 0
	for row in self.buffer[0:8]:
	    self.grid1.disp.setBufferRow(n, row, False)
	    n = n + 1
	n = 0
	for row in self.buffer[8:16]:
	    self.grid2.disp.setBufferRow(n, row, False)
	    n = n + 1
	self.grid1.disp.writeDisplay();
	self.grid2.disp.writeDisplay();
        self.ticker[len(self.ticker):] = []
        self.buffer[len(self.buffer):] = []
        self.display[len(self.display):] = []
     
    def main(self):
        self.scrolling_ticker_text()
        self.update_ticker_w_buffer() 
        #self.grid1.disp.clear()
        #self.grid2.disp.clear()
