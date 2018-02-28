'''
Created on 27 Jan 2015

@author: cuddlyteddy
'''
# definiting function shut_down(s) take takes argument s in parentheses

def shut_down(s):

    if (s =="yes"):
        print ("Shutting Down")
    elif(s == "no"):
        print ("Shutdown aborted")
    else:
        print ("sorry")
# getting raw input from the user 
# raw_input is not valid instead you need to use input(prompt)
s = input("Enter the word")
# assign variable name s lowercase value (.lower())
s = s.lower()
print (s)
# calling shut_down function
shut_down(s)