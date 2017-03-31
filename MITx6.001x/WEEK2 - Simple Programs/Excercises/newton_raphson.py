# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:17:18 2017
"""
#Newton-Raphson for y = x^2+k

epsilon = 0.01
y = 24.0
guess = y/2.0
numguess = 0

while abs(guess*guess-y) >= epsilon:
    numguess +=1
    guess = guess - (((guess**2 - y)/(2*guess)))
    print(guess)
print('guesses = ' + str(numguess))
print('Sqrt of ' +str(y) + ' is about ' + str(guess))
 
