#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())


# python3 Captilize.py < list_ex
#  this will capitalize the starting letter of each line in list_ex