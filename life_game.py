""" Life Game"""

def start():
	print "Life Game"
	print "Enter player name"
	player_name = raw_input("> ")
	print "%s is sitting on a chair next to desk." % player_name
	print "Thinking what I should do?"
	player_input = raw_input("> ")
	player_input = player_input.split()
	print player_input
	
	arrays = ["laptop", "open"]

	if all(arrays in player_input):
		open_laptop(player_name)
	else:
		print "no"	

def using_laptop(player):
	print "Laptop is start\nUser has three choice"
	print "1 Open internet browser"
	print "2 play game"
	print "3 Work"
	player_input = raw_input("> ").split()
	if 1 in player_input or browser in player_input:
		print "hello hello"
	else:
		print "no really"	


def internet_browser():
	print "Browser is open.\nUser has two choice"
	print "1 Study using Internet resource."
	print "2 Watch entertainment videos such as movies, anime or simply youtube video."

	player_input = raw_input("> ").split()

	if 1 in player_input or "Study" in player_input:

		print "You started studying.\nTo be continued....."

	elif 2 in player_input or "entertainment" in player_input or "anime":
		print "rem"

	else:
		print "I got bored"	

def open_laptop(player):
	print "%s opened laptop." % player
	print "The laptop is nearly out of battery!"
	player_input = (raw_input("> ")).split()

	if "take" in player_input or "pick" in player_input and "charger" in player_input and "charge" in player_input:
		print "Charging laptop"
		start()
	elif "take" not in player_input or "pick" not in player_input :
		print "You don't have charger with you."
		player_input = raw_input("> ").split()
		if "take" in player_input or "pick" in player_input and "charge" in player_input:
			print "Laptop charging"
		else:
			print "Laptop died"
# start game
start()	