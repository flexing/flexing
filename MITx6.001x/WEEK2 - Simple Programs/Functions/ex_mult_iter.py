# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:40:35 2017
"""
def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a 
        b -= 1
        print(a,b,result)
    return result
