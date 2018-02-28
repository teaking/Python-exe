# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
hrs = 0
mins = 0
millisecs = 0
secs = 0
timers=0;
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(str(hrs)+":"+str(mins)+":"+str(secs)+":"
                     + str(millisecs), [50,50], 48, "Red")

def timer_handler():
    global timers
    timers+=1
    format(timers)
    
def stop_handler():
    timer.stop()

def start_handler():
    timer.start()
    
def reset_handler():
    global timers
    timers=0

def format(t):
    global hrs, mins, secs, millisecs
    millisecs = millisecs // 100
    secs = millisecs % 100
    mins = secs % 60
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("X", 400, 400)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(0.1,timer_handler)
frame.add_button("stop",stop_handler)
frame.add_button("start",start_handler)
frame.add_button("resets",reset_handler)
# Start the frame animation
frame.start()
timer.start()

