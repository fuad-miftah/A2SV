#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
if __name__ == '__main__':

    n = int(input().strip())
    a = list(map(int , input().rstrip().split()))
    swapTimes = 0
    for i in range(len(a)-1):
        swap = 0
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapTimes = swapTimes + 1
                swap = swap + 1
        if swap == 0:
            break

    print("Array is sorted in {} swaps.".format(swapTimes))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]))
