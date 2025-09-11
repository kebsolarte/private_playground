from turtle import Turtle, Screen
import colorgram
import random

# Get base colors from sample image and create a list of rgb tuples
colors = colorgram.extract('sample.jpg', 10)
colors_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# Creating turtle object
pointer = Turtle()
pointer.penup()
pointer.shape("circle")
pointer.speed("fast")

# Creating screen object
screen = Screen()
screen.colormode(255)

# Creating function to draw dots
def draw_dot(size):
    color = random.choice(colors_list)
    pointer.dot(size, color)

# Setting initial position of turtle object to lower left
position = [-200, -200]

# Main loop for drawing 10x10 dots array
for i in range(1,11):
    position[1] += 50.00
    new_position = tuple(position)
    pointer.setpos(new_position)

    for i in range(1,11):
        draw_dot(20)
        pointer.forward(50)

# Hiding the turtle object after dot painting
pointer.color("white")

screen.exitonclick()