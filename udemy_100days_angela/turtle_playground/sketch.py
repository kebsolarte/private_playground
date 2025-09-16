# Creating a simple etch-a-sketch program
from turtle import Turtle, Screen

# Create turtle and screen objects
pointer = Turtle()
screen = Screen()

# Defining movement functions
def forward():
    pointer.forward(100)

def backward():
    pointer.backward(100)

def turn_right():
    pointer.setheading(pointer.heading() - 30)

def turn_left():
    pointer.setheading(pointer.heading() + 30)

def clear():
    screen.resetscreen()

# Defining key bindings
screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="c", fun=clear)



screen.exitonclick()

