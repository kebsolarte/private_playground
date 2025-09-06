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

def draw_dot(size):
    color = random.choice(colors_list)
    pointer.dot(size, color)


position = [-200, -200]

for i in range(1,11):
    position[1] += 50.00
    new_position = tuple(position)
    pointer.setpos(new_position)

    for i in range(1,11):
        draw_dot(20)
        pointer.forward(50)

pointer.color("white")

screen.exitonclick()