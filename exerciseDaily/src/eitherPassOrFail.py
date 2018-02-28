'''
Created on 29 Jan 2015

@author: cuddlyteddy
'''

'''
Write a program called CheckPassFail which prints "PASS" 
if the int variable "mark" is more than or equal to 50; or prints
"FAIL" otherwise.
'''
#    mark needed to pass the exam
neededToPass =50
name = input("Enter your name here")
mark = int(input("Enter your mark here"))

# condition if the mark is higher than the 50 it needs to print if statement otherwise print else statement
if(mark >= neededToPass):
    print (("Be Glad you Pass the Exam. %s you got %s") % (name, mark))
else:
    print (("Sorry to tell you %s you fail the exam. You only got %s mark") % (name,mark))
    
   