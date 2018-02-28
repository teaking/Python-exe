'''Dictionary Data Structure example'''

#create a mapping of state to abbreviation

states = {
	'Oregon': 'OR',
	'Florida':'FL',
	'California':'CA',
	'New York': 'NY',
	'Michigan':'MI'
}

cities = {
	'CA': 'Sans Fransisco',
	'MI': 'Detroit',
	'FL':'Jacksonville'

}

#add some more cities

cities['NY'] = "New York"
cities['OR'] = 'Portland'

#print out some cities

print '_' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#do it by using the state then cities dict
print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation

print'_' * 10

for state, abbre in states.items():
	print "%s is abbreviated %s" % (state, abbre)

print '_' * 10

for abbrev, city in cities.items():
	print "%s has the city %s" %(abbrev, city)	

print '_' * 10

for state, abbre in states.items():
	print "%s state is annreviated %s and has city %s" % (state, abbre,cities[abbre])

print '_' * 10

# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "false"
else:
	print "true"		

#get a city if not output the default value
city = cities.get('OR', 'Does Not Exist')
print "The city for the state 'OR' is: %s" % city	

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city	

print cities

print cities.pop('OR')

print cities
