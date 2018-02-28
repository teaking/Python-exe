# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:39:07 2017

@author: blindness

convert decimal to hexadecimal 
"""

def to_string(n, base):
    convert_string = "0123456789ABCDEF"
    if(n < base):
        return convert_string[n]
    else:
        return to_string(n/base,base) + convert_string[n % base]
        
print(to_string(2835,16))        