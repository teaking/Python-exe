'''
Created on 30 Jan 2015

@author: cuddlyteddy
'''
# create a list named dog with three strings
dog = ["German Shepard", "Bull Dog", "Chiwawa"]
# create a list named dogBabies with three strings
dogBabies = []
# looping by using for loop 
for index in dog:
   
    dogBabies.append(index + " you are my dog")
    dogBabies.sort()
    print (dogBabies)