# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:43:21 2017

@author: blindness
"""

def isLunchTime(hour):
    if hour > 1 and hour < 12:
        return True 
    else:
        return False
        
print isLunchTime(23)