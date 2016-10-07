# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:53:54 2016

@author: skotiang
"""

def primeNumbers(n): 
    
    prime = 2   # the initial prime number
    
    result_prime = [prime]  # initialize the output sequence
    
    while prime < n:
        prime += 1
        
        for index in result_prime:
            if prime%index == 0:
                break
            else:
                if prime not in result_prime:
                    result_prime.append(prime)
                    
    print result_prime

    
    
    
   

    
    
    
    


    
    