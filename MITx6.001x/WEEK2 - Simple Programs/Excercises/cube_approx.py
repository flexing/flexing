# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:57:06 2017
"""
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.001
numguess = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    numguess += 1
print("num of guesses=", numguess)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to cube root of", cube)
    
