'''
Created on 22 Feb 2015

@author: cuddlyteddy
'''
listing = [1,6,8,9] # list
print (listing) # print list no need index like  in c 
for x in range(1,20): # for loop loop 1 till 20
    if x in listing:# looks at in listing and compares the x with listing value
        continue# continue looping instead of breaking (break)
    print (x)# prints the result
