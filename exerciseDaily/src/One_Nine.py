'''
Created on 30 Jan 2015

@author: cuddlyteddy
'''

'''
Write a program called PrintNumberInWord which 
prints "ONE", "TWO",... , "NINE", "OTHER" if the int 
variable "number" is 1, 2,... , 9, or other, respectively. 
Use (a) a "nested-if" statement; (b) a "switch-case" statement.
'''
#creating function called one_nine that reads the user input
n = input("Enter the Number here 0 -9")
# looks at the number not needed though
def one_nine(n):
    y = int(n) * 3
    return y
    
# creating function that checks what number it is and give it's value

def value (n):
    if(one_nine(n) == 1):
        print("one")
    elif(one_nine(n) == 2):
        print("Two")
    elif(one_nine(n) == 3):
        print("Three")
    elif(one_nine(n) == 4 ):
        print("Four")
    elif(one_nine(n) == 5 ):
        print("Five")
    elif(one_nine(n) == 6 ):
        print("Six")
    elif(one_nine(n) ==7):
        print("Seven")
    elif(one_nine(n) == 8 ):
        print("Eight")
    elif(one_nine(n) == 9 ):
        print("Nine")
    elif(one_nine(n) == 0 or one_nine(n) > 9 ):
        print("You are not listening to me!")
value(n)           


    