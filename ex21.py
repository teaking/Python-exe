# returning from function 

def add(a, b):
	print "Adding %d + %d." % (a, b)
	return a + b


def subtract(a, b):
	print "Subtracting %d - %d." % (a, b)
	return a - b	

def multiply(a, b):
	print "Multiplying %d x %d." % (a, b)
	return a * b

def divide(a, b):
	print "Dividing %d / %d." % (a, b)
	return a / b

def modulo(a, b):
	print "Modulos %d  %d." % (a, b)			
	return a % b

age = add(30, 5)
height = subtract(70, 4)
weight = multiply(90, 2)
iq = divide (100, 2)
pay = modulo(10, 2)

print "Age: %d, Height: %d, Weight %d, IQ: %d, Pay: %d" %(age, height, weight, iq, pay)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print "That becomes: ", what , "Can you do it by hand?"

