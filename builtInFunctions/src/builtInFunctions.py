'''
Created on 27 Jan 2015

@author: cuddlyteddy
'''

''' there is some error in the type(s) == int check it out late'''
# defining function called distance_from_zeros which takes the
# argument inside its parentheses
def distance_from_zero(s):
# if condition is true run the code 
# type checks what type of value it is 
# and abs() allows absolute values (positive number)
    if (type(s) == int):
        print("hey" )
# else run this code
    else:
        print(s)

# getting user input
s = input("enter the number between 0 to 9")
# calling function
distance_from_zero(s)

y = 100
if(type(y) == int):
    print ("hello world")
