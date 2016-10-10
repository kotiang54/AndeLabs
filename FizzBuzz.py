# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 23:21:20 2016

@author: skotiang
"""

def fizz_buzz(argument):
    
    """ A function that returns "Fizz", "Buzz", or "FizzBuzz", depending on the argument 
         of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.
    """
    if argument <= 0:
        raise ValueError
    
    if argument % 3 == 0 and argument % 5 != 0:   # return the sound "Buzz" if its divisble by 3
        return "Fizz"
        
    elif argument % 5 == 0 and argument % 3 != 0:  # return the sound "Buzz" if its divisble by 5
        return "Buzz"
        
    elif argument % 3 == 0 and argument % 5 == 0:   # return the sound "FizzBuzz" if its divisble by both 3 & 5
        return "FizzBuzz"
        
    elif argument % 3 != 0 and argument % 5 != 0:   # return the number if its indivisble by both 3 & 5
        return argument
    
