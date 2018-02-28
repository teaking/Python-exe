'''
Created on 22 Feb 2015

@author: cuddlyteddy
'''
name = input("Enter your name")
print ("Is you name %s" % (name))
ip = input("%s or %s" % ("yes","no"))
if(ip == "yes".lower() or ip == "y".lower()):
    print ("you liar")
else:
    print("good")
val = 50
while(val > 1):
    value = input("pick the number")
    val -= int(value)
    print ("your value is %d"%(val))
    if(val < 0):
        print ("error")
    else:
        print ("%s" %("game over")) # try to make function and use that function to loop again if the error comes