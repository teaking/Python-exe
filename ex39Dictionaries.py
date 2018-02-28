# Dictonaries data structure
things = ['a', 'b', 'c', 'd']
print things [1]

things[1] = 'z'
print things[1]
print ' '.join(things)
print things 
print "Above using just list"
print "Below we are using Dictionaries Data Structure."

stuff  = {'name':'zed', 'age':39, 'height': 6 * 12 / 2}

print stuff['name']

print stuff['age']

print stuff['height']

stuff['city'] = "San Franscisco"

print stuff['city']

print "stuff"
print stuff

print "Adding element with integer as a key stuff[0] = \"Zero\""
stuff[0] = "Zero"
print "Get element using number"

print stuff[0]

print "stuff"
print stuff

print "Deleting element using del keyword."

del stuff['city']
print "stuff"
print stuff

del stuff[0]
print "stuff"
print stuff