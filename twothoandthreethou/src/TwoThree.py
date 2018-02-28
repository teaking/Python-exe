'''
Created on 22 Feb 2015

@author: cuddlyteddy
'''
from macpath import join
l = [] # creating a list 
for x in range (1, 200): # x is similar to i (for loop) range between 1 to 200
    if (x % 7 == 0 and x % 5 == 0):# if x is multiple of 7 and 5 get the value
       l.append(str(x))# add x which is string now due to (str) in the l 
       print (' , '.join(l))# add "," comma in l 
