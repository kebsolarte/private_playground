from turtle import Turtle, Screen
import colorgram

# Get base colors from sample image and create a list of rgb tuples
colors = colorgram.extract('sample.jpg', 10)
colors_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]


# Creating turtle object
pointer = Turtle()
pointer.shape("circle")
pointer.speed("fast")

# Creating screen object
screen = Screen()
screen.colormode(255)









screen.exitonclick()