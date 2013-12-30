#!/usr/bin/python
# source: https://github.com/pdp7/beaglebackpack/blob/master/README.md

import argparse
import string2text as str2mat
app_text = str2mat.Text2LED() # initialize test to test app
app_ticker = str2mat.LED_TICKER() # Initialize LED ticker

parser = argparse.ArgumentParser(description='scroll message on Adafruit I2C 8x8 LED matrix displays')
parser.add_argument('-r', '--repeat', action='store_true', default=False, help='message will repeat forever')
parser.add_argument('-v', '--verbose', action='store_true', default=False, help='output diagnostic information')
parser.add_argument('message', nargs="*", help='message to scroll')

args = parser.parse_args()
message = " ".join(args.message)

if(args.verbose == True):
    print args.message
    print "message: " + message

while True:
    # scroll the message on the displays
    app_ticker.ticker = app_text.add_to_ticker(message + " ")
    app_ticker.main()
    # if repeat flag is False then don't repeat the message
    if(args.repeat == False):
        break;
