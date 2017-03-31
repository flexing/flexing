# -*- coding: utf-8 -*-
"""
Course: MITx 6.001x Problem Set 1, Part 2

"""
s = 'zbbbobbbobbsbbobobob'
hit = 'bob'
count = 0

for char in range(len(s)):
    if s[char:char+3] == hit:
        count += 1

print("Number of times 'bob' occurs is " +  str(count))

#correct
