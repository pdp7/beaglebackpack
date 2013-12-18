#!/usr/bin/python

import time
import datetime
import facebook
from Adafruit_7Segment import SevenSegment

# ===========================================================================
# title: beaglebone black with adafruit 7-segment facebook notifications display
# author: drew fustini (http://element14.com/fustini)
# blog: http://www.element14.com/community/community/knode/single-board_computers/next-gen_beaglebone/blog/2013/11/08/beaglebone-black-displays-facebook-notifications-on-adafruit-7-segment
#
# method 1: get short term (2 hour) access_token from:
#    https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Fnotifications
# method 2: get extended (60 days) access_token via instructions at:
#    http://fearofcoding.blogspot.com/2012/10/python-script-to-fetch-messages-from.html
#    note: install the needed python module with "pip install facepy"
# ===========================================================================

access_token = "CAAH9yZAk1AN8BABX35A2uZCvySRZAP00qrEsn9CcrHmvMChvXn8EuwnQvHN0tlI4SF2gWvfBTjWZAW3gYcHXhc2qutPgRBGF7V6u85mTsFRvNk96h3fg9rYtObZCkV8wd000ubiVTKXw5qiuGWKztmbeolxTWDh2O5gzQvdr3Pf3wyuLb0cVMqe8pGWx5GF8ZD"

segment = SevenSegment(address=0x70)

print "Press CTRL+C to exit"

# Continually update the current unseen notification count on a 4 char, 7-segment display
while(True):
  segment.disp.setBufferRow(0, 0);
  segment.disp.setBufferRow(1, 0);
  segment.disp.setBufferRow(2, 0);
  segment.disp.setBufferRow(3, 0);
  segment.disp.setBufferRow(4, 0);

  graph = facebook.GraphAPI(access_token)
  notifications  = graph.get_object("me/notifications")
  print "notifications"
  summary = notifications['summary']
  print "summary"
  print summary
  if summary:
    num = summary['unseen_count']
    print num
    print int(num / 10)
    d0 = int(num / 1000)
    d1 = int(num / 100)
    d3 = int(num / 10)
    d4 = num % 10
    if d0 != 0:
      segment.writeDigit(0, int(num / 1000 ))
    if d1 != 0 or num >= 1000:
      segment.writeDigit(1, int(num / 100))
    if d3 != 0 or num >= 100:
      segment.writeDigit(3, int(num / 10))
    if d4 != 0 or num >= 10:
      segment.writeDigit(4, num % 10)
  time.sleep(60)
