# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:36:07 2017
"""

def mult(a,b):
    if b == 1:
        return a
    else:
        return a * mult(a, b-1)