#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n -= 1
    s_3 = ((n//3)/2)*(3+3*(n//3))
    s_5 = ((n//5)/2)*(5+5*(n//5))
    s_15 = ((n//15)/2)*(15+15*(n//15))
    s = s_3+s_5-s_15
    print(int(s))
