# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 23:20:42 2016

@author: skotiang
"""

def data_type(argument):
    """
    A function that compares and return results, based on the argument ...
    supplied to the function
    """
    if argument == None:     # returns a string "no value" for input argument "None"
        return 'no value'
        
    elif type(argument) == list and len(argument) > 2:
        return argument[2]          # return the 3rd item of the list
        
    elif type(argument) == list and len(argument) <= 2:
        return None
        
    elif type(argument) == bool:   # return the booloean for a boolean type argument
        return argument
        
    elif type(argument) == int:   # return less than or more than 100 if argument is integer type
        if argument < 100:
            return 'less than 100'
            
        elif argument == 100:
            return 'equal to 100'
            
        else:
            return 'more than 100'
            
    elif type(argument) == str:    # returns the length of string if the argument is string type
        return len(argument)