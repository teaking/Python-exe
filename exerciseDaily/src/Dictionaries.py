'''
Created on 31 Jan 2015

@author: cuddlyteddy
'''
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], 
    # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
'''
inventory = {104:"pocket"}
#creating a new entry and add vaue in it
inventory["pocket"]= ["seadshell","strange berry", "lint"]

# Sorting the list found under the key 'pouch'
#inventory["pouch"].sort() 
inventory["backpack"].sort()
# removing the "dagger" value from backpack list
inventory["backpack"].remove("dagger")
#storing new value in to the gold key which is in the inventory #list
'''
inventory["pocket"] = "knife","glass","scissor"
inventory["backpack"].sort()

print (inventory)
d = {"foo" : "bar"}

for key in d: 
    print (d[key]) 