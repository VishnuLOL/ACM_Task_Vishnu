#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a,b=0,1
    i=0
    num=[]
    while i<n:
        if a%2==0:
            num.append(a)
        c=a+b
        a=b
        b=c
        i=a
    print(sum(num))
