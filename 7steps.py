# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

#define global variables (program state)
counter=0

#define "helper" functions
def increment():
    global counter
    counter+=1

def print_goodbye():
    msg="Goodbye"
    print msg
    
#define event handler functions 
def tick():
    increment()
    print counter
    
def clicked():
    print_goodbye()
#create a frame
frame=simplegui.create_frame("simpleGUI test",100,100)
frame.add_button("click me", clicked)
#register event handlers
timer=simplegui.create_timer(1000,tick)
#start frame and timers
frame.start()
timer.start()
