import turtle

def draw_square(some_shape):
    some_shape.color("yellow")
    some_shape.shape("turtle")
    for num in range(0,100):
        for num in range(0,4):
            some_shape.forward(100)
            some_shape.right(90)
        some_shape.right(10)    


def art():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    draw_square(brad)
    pete = turtle.Turtle()
    pete.circle(100)
    
    window.exitonclick()

art()
