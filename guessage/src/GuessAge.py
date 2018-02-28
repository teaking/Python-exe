'''
Created on 22 Feb 2015

@author: cuddlyteddy
'''
val =int( input("enter the value"))
val *= 2
print(val)
val += 5
val *= 50
ip =input("Do you already have your birthday? \n if yes enter \"y\" else \"n\"")
if(ord(ip) == 121):
    val += 1765
    nip =int(input("Enter the dob "))
    val -= nip
    print(val)
else:
    val +=1764
    nip =int(input("Enter the dob "))
    val -= nip
    print (val)