#!/usr/bin/python

import time
import datetime
import facebook
import sys
from Adafruit_8x8 import EightByEight

# ===========================================================================
# title: beaglebone black with adafruit 8x8 LED matrix facebook notification display
# author: drew fustini (http://element14.com/fustini)
# blog: http://www.element14.com/community/community/knode/single-board_computers/next-gen_beaglebone/blog/
#
# method 1: get short term (2 hour) access_token from:
#    https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Fnotifications
# method 2: get extended (60 days) access_token via instructions at:
#    http://fearofcoding.blogspot.com/2012/10/python-script-to-fetch-messages-from.html
#    note: install the needed python module with "pip install facepy"
# ===========================================================================

access_token = "CAAH9yZAk1AN8BABX35A2uZCvySRZAP00qrEsn9CcrHmvMChvXn8EuwnQvHN0tlI4SF2gWvfBTjWZAW3gYcHXhc2qutPgRBGF7V6u85mTsFRvNk96h3fg9rYtObZCkV8wd000ubiVTKXw5qiuGWKztmbeolxTWDh2O5gzQvdr3Pf3wyuLb0cVMqe8pGWx5GF8ZD"

grid = EightByEight(address=0x70)

print "Press CTRL+C to exit"

# Continually update the current unseen notification count on a 4 char, 7-segment display
while(True):
  grid.clear()
  graph = facebook.GraphAPI(access_token)
  notifications  = graph.get_object("me/notifications")
  print "notifications"
  print notifications
  summary = notifications['summary']
  if summary:
    num = summary['unseen_count']
    print num
    min=0
    max=8
    fullRows=0

    for n in range(0, 8):
      if num > min and num <= max:
        for y in range(0, 8):
	  for x in range(0, fullRows):
            grid.setPixel(x, y)
        for y in range(0, num-min):
          grid.setPixel(fullRows, y)
      min+=8
      max+=8
      fullRows+=1

  time.sleep(60)
