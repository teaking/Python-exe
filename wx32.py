the_count = [1,2,3,4,5,6]
fruits = ['apples', 'oranges', 'pears', 'banana']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for loop 
for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

for i in change:
	print "I got %r" % i		

elements = []

for i in range(0, 10):
	print "Adding %d to the list." % i
	elements.append(i)

for i in elements:
	print "Elements was: %d" % i

# adding number from 0 to 49
num = range(0, 50)

for i in num:
	print "num contains %d." % i