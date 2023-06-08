#!/usr/bin/python3

import sys
arguments = sys.argv[1:]
sum_result = 0

for arg in arguments:
    sum_result += int(arg)
print("{}".format(sum_result))
