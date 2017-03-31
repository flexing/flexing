# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:21:55 2017
"""
#Werner Krauth - monte carlo pi
from random import uniform

def d_pi(N):
    nhits = 0
    for i in range(N):
        x, y = uniform(-1.0, 1.0), uniform(-1.0,1.0)
        if (x **2 + y **2) < 1.0:
            nhits += 1
    return nhits

ntrials = 10000
for attempt in range(10):
    print(attempt, 4*d_pi(ntrials)/float(ntrials))