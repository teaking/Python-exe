# function and variable
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You hace %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# passing number as argument to the function
cheese_and_crackers(20, 30)

print "OR, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# passing variable as an argumnet for the function
cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print"we can even do math inside too:"
# add number to the variable and pass it as an argument
cheese_and_crackers(10+amount_of_cheese, 10 + amount_of_crackers)
