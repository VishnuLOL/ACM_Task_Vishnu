#!/bin/python3

import sys


t=int(input().strip())
for a0 in range(t):
    n=int(input().strip())
    pl=[]
    for i in range(101,1000):
        for j in range(121,1000,(1 if i%11 == 0 else 11)):
            p=i*j
            s=str(p)

            if s==s[::-1]:
                if p<n:
                    pl.append(p)
    print(max(pl))
