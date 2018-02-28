'''
Created on 29 Jan 2015

@author: cuddlyteddy
'''

'''
Write a program called CheckOddEven which prints 
Odd Number if the int variable number is odd, 
or Even Number otherwise.
'''
# store the user input in the varaible named number 
# int(input("Enter the number")) declares the user input data type to be int
number = int(input("Enter the number"))
# Any number that is divisible by two is even and gives no remainder thus the remainder should be 0 
if(number % 2 != 0):
    print (("%s is a ODD NUMBER!") %(number))
else:
    print(("%s is a EVEN NUMBER!") % (number))
    