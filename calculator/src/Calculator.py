# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
store = 0
operand = 0
        
# Define "helper" functions
def output():
    global store,operand
    print ("store: " + str(store))
    print ("operand: " + str(operand))
    print ("")
# Define event handler functions
def add():
    print ("Adding")
    global store, operand
    store = store + operand
    output()

def sub():
    print ("Subtract")
    global store, operand
    store = store - operand
    output()
    

def divide():
    print ("Divide")
    global store, operand
    store = store / operand
    output()
    

def multiple():
    print ("Multiple")
    global store, operand
    store = store * operand
    output()
    
def swap():
    print ("Swapping")
    global firstNumber, secondNumber
    firstNumber, secondNumber = secondNumber, firstNumber
    output()
    
def c():
    global store, operand
    print ("Resetting the value to 0")
    store = 0
    operand = 0
    output()
    
def showNumber():
    print ("Showing current Number")
    output()
def sto(inp):
    global store
    store = float(inp)
def ope(inp):
    global operand
    operand = float(inp)
# Create a frame
frame = simplegui.create_frame("Calculator",200,350)

"""
adding button
"""
frame.add_button("+",add,50)
frame.add_button("-",sub,50)
frame.add_button("X",multiple,50)
frame.add_button("/",divide,50)
frame.add_button("Swap",swap,50)
frame.add_button("C",c,50)
frame.add_button("S_NO.",showNumber,50)
"""
INPUT
"""
frame.add_input("STORE: ",sto,100)
frame.add_input("OPERAND",ope,100)
# Register event handlers

# Start frame and timers
#frame.start()
