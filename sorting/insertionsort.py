#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, len(arr)):
        curr = arr[i]
        insertAt = i
        for j in range(i-1,-1,-1):
            if curr < arr[j]:
                arr[j+1] = arr[j]
                insertAt = j
                print(*arr)
        if insertAt != i:
            arr[insertAt] = curr
            print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
