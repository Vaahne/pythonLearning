#!/usr/bin/env python3

import sys

for line in sys.stdin:
    words = line.strip().split()
    print(" ".join([word.capitalize() for word in words]))

# To run this script
# cat test.sh | python3 test_capital.py
# this will capitalize each word of the file test.sh and prints

# python3 test_capital.py < test.sh

#  in bash
# for i in $(cat story.txt); do
#  B=`echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"`; echo -n "${B}${i:1} "; done; echo -e "\n"