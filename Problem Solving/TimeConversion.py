#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ampm = s[8:10]
    if ampm.upper() == 'PM':
        if s[0:2] == '12':
            return '12' + s[2:8]
        else:  
            hour = int(s[0:2])
            hour += 12
            hour = str(hour)
            return hour + s[2:8]
    if ampm.upper() == 'AM' and s[0:2] == '12' and s != '12:00:00AM':
        return '00' + s[2:8]
    if s == '12:00:00AM':
        return '00:00:00'
    else:
        return s[0:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    fptr.write(result + '\n')

    fptr.close()
