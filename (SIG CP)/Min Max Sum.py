#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    a,b=arr[1],arr[1]
    s_min,s_max=0,0
    for i in range(len(arr)):
        if arr[i]>a:
            a=arr[i]
    for i in range(len(arr)):
        if arr[i]<b:
            b=arr[i]
    s=sum(arr)
    s_min=s-a
    s_max=s-b
    
    print(s_min,s_max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
