"""
create a rock Paper Scissor game

"""

import random

def userChoice2Number(userInput):
    """
    change the user input to the number so that we can compare it
    with the randomize generated number.
    """
    if(userInput == "SCISSOR"):
        return 0
    elif(userInput == "PAPER"):
        return 1
    elif (userInput == "ROCK"):
        return 2
    else:
        print ("Did not choose the requested one so terminating!")
        
def compareUserChoice2ComputerInput(userInput,ComputerInput): 
    """
    comparing user Input with computer randomize generated number
    """
    if(userInput == 0 and ComputerInput == 0):
        return "Both use Scissor - draw"
    elif(userInput == 0 and ComputerInput == 1):
        return "User won with scissor to the paper"
    elif(userInput == 0 and ComputerInput == 2):
        return "Computer won with rock to the scissor"
    elif(userInput == 1 and ComputerInput == 0):
        return "Computer won with scissor to the paper"
    elif(userInput == 1 and ComputerInput == 1):
        return "Both users Paper - draw"
    elif(userInput == 1 and ComputerInput == 2):
        return "User won with paper to the rock"
    elif(userInput == 2 and ComputerInput == 0):
        return "user won with rock to the scissor"
    elif(userInput == 2 and ComputerInput == 1):
        return "computer won with paper to the rock"
    else:
        return "both uses rock - draw"
    
    
userInput = input("Please Input your choice \"scissor, Paper, Rock\"")
#ask user what they want to use
userInput = userInput.upper()
#changing the value to uppercase so that later we don't need to stuck in error
ComputerInput =random.randint(0, 2)
#generating randomise number

"""
main 
"""
userInput = userChoice2Number(userInput)
if(userInput == 0 or userInput == 1 or userInput == 2):
    print (compareUserChoice2ComputerInput(userInput,ComputerInput))
else:
    print ("Input needs to be scissor, paper or rock")
    

