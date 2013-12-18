#!/usr/bin/python
''' Created on Oct 10, 2013
@author: matthassel
'''
import string2text as str2mat
from threading import Thread
from time import sleep
from copy import copy
from sys import exit
app_text = str2mat.Text2LED() # initialize test to test app
app_ticker = str2mat.LED_TICKER() # Initialize LED ticker
            
while True:
	app_ticker.ticker = app_ticker.ticker + app_text.add_to_ticker("HAPPY HOLIDAYS!", "green")
	app_ticker.main()
     
