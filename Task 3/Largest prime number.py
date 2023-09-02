#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    f = []
    pf = []
    for i in range(1, n+1):
        if n % i == 0:
            f.append(i)
    for i in f:
        c = 0
        for j in range(1, i+1):
            if i % j == 0:
                c += 1
        if c == 2:
            pf.append(i)
    print(max(pf))
