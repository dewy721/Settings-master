#!/usr/bin/python

import sys
import linuxcnc
try:
    s = linuxcnc.stat(dtg) # create a connection to the status channel
    s.poll() # get current values
except linuxcnc.error, detail:
    print "error", detail
    sys.exit(1)
for x in dir(s):
    if not x.startswith('_'):
        print x, getattr(s,x)