'''
Created on 27 Jan 2015

@author: cuddlyteddy
'''
# defining function called one that returns value n * 2
def one(n):
    y = int(n) + 2
    return y
# defining 2nd function called two that prints out the result.
def two(n):
    print (one(n))
# getting input from the user
# storing input value to n
n = input("Enter the numerical value!")

# calling function 
two (n)