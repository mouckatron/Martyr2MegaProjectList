#! /usr/bin/python2.7

import os
import sys

data = sys.stdin.read().strip()

if data == data[::-1]:
    sys.exit(0) # 0 is true or no failure
else:
    sys.exit(1) # 1 is false or failure
