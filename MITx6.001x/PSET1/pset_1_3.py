# -*- coding: utf-8 -*-
"""
Course: MIT 6.001x Problem Set 1, Part3

"""
#Correct (1/1 point)

s = 'azcbobobegghakl'
maxc = 0
count = 0
result = 0

for i in range(len(s)-1):
    
    if (s[i]<= s[i+1]):
        count = count + 1
        if count > maxc:
            maxc = count
            result = i + 1
    else:
        count = 0
        
start = result - maxc
print("Longest substring in alphabetical order is:", s[start:result+1])
    










