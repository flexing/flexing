# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:52:08 2017
"""
#bisection search - find secret number
high = 100
low = 0
print("Please think of a number between 0 and 100!")

while True:
    ans = ((high + low)//2)
    print("Is your secret number " + str(ans) + "?")
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if user == 'c':
        print("Game over. Your secret number was:", ans)
        break
    elif user == 'h':
        high = ans
    elif user == 'l':
        low = ans
    else:
        print("Sorry, I did not understand your input.")

