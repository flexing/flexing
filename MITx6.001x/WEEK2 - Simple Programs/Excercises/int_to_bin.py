# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:06:31 2017
"""
#Int -> binary number

n = -2

if n < 0:
    isNeg = True
    n = abs(n)

else:
    isNeg = False

result = ''

if n == 0:
    result = '0'

while n > 0:
    result = str(n%2) + result
    n = n//2

if isNeg:
    result = '-' + result
print(result)