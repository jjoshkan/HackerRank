#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    i = 0
    while i < len(c):
        if i == len(c) - 1:
            break
        elif i == len(c) - 2:
            jump += 1
            i += 1
            break
        if c[i+2] == 1:
            jump += 1
            i += 1
        else:
            jump += 1
            i += 2
    return jump
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
