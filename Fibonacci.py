# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:22:26 2016

@author: skotiang
"""
        

from math import sqrt    # importing the math formular

def Fibonacci_nums(n):
    
    sequence = list()
    
    X = (1 + sqrt(5))/2
    Y = (1 - sqrt(5))/2
    
    for index in xrange(n):
        
        term = int((X**index - Y**index)/sqrt(5))    # Fibonacci recursive algorithm
        sequence.append(term)     # append the nth term to the sequence
        
    print sequence
        
    