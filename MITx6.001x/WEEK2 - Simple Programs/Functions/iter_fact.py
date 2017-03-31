# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:41:38 2017
"""

def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod