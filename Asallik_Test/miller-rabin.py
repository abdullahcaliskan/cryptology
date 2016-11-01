#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random

def modexp(a,b,n):
    r = 1
    while 1:
        if (b % 2) == 1:
            r = (r * a) % n
        b = int (b / 2)
        if (b == 0):
            break
        a = (a * a) % n
    return r

def usBul(n):
    s = 1
    r = (n-1) / (2 ** s)
    while type(r) == float:
        s += 1
        r = (n-1) / (2 ** s)
    return s

def aVer(n):
    a = random.randrange(2,n-2)
    while math.gcd(a,n) != 1:
        a = random.randrange(2,n-2)
    return a

def yHesapla(a,r,n):
    y = (a ** r)
    return y % n

stat = 0
n = 12886
t = 3
j = 0
for i in range(0,t):
    s = usBul(n)
    print ('s:',s)
    r = (n-1) / (2 ** s)
    print ('r:',r)
    a = aVer(n)
    print ('a:',a)
    y = yHesapla(a,r,n)
    print ('y:',y)
    if y != 1 and y != n-1:
        j = 1
        while j <= s-1 and y != n-1:
            y = yHesapla(y,2,n)
            if y == 1:
                print ('Composite, Asal Degil')
                stat = 1
            j += 1
        if y != (n-1):
            print ('Composite, Asal Degil')
            stat = 1
if stat == 0:
    print ('Prime, Asal')
