# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:23:38 2017

@author: blindness
"""

def name_to_number(name):
    if(name == "rock"):
        return 0
    elif(name =="Spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif(name=="lizard"):
        return 3
    elif(name=="scissors"):
        return 4
    else:
        return "name not recognised"
        

print type(name_to_number("rock"))

def num_to_name(num):
    if(num==0):
        return "rock"
    elif(num==1):
        return "Spock"
    elif(num==2):
        return "paper"
    elif(num==3):
        return "lizard"
    elif(num==4):
        return "scissors"
    else:
        return "num not recognised"
        
print num_to_name(2)

def rspsl(player_choice):
    print("")
    print "Player chooses",player_choice
    player_choice=name_to_number(player_choice)
    comp_choice=random.randrange(0,5)
    num_to_name(comp_choice)
    print "Computer chooses",num_to_name(comp_choice)
    choice_val = (comp_choice - player_choice)%5
    #modulo to loop back to always get value less than 5
    if(choice_val >= 1 and choice_val <= 2):
        print "computer wins"
    elif(choice_val == 0):
        print "draw battle"
    else:
        print "player wins"    

rspsl("rock")
rspsl("Spock")
rspsl("paper")
rspsl("lizard")
rspsl("scissors")    