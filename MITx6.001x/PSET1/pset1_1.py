# -*- coding: utf-8 -*-
"""
Course: MIT 6.001x Problem Set 1, Part1

Problem 1
10.0 points possible (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5"""


s = 'azcbobobegghakl'
numv = 0
for char in s:
    if char == 'a' or char =='e' or char == 'i'\
    or char =='o' or char == 'u':
        numv = numv + 1
print("Number of vowels: " + str(numv))

#correct
