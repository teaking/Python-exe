# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:16:01 2018

@author: blindness
"""

from bresenham import bresenham
#The bresenham(x0, y0, x1, y1) function, 
#which returns a generator of the coordinates of the line from (x0, y0) to (x1, y1).
print(list(bresenham(-1,1,2,-2)))
