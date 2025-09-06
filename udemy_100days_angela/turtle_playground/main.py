import random
from turtle import Turtle, Screen

# Creating a Turtle object
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSlateGray4")
timmy.speed("fastest")

# Creating screen object
screen = Screen()
screen.colormode(255)

# Moving the Turtle
def forward_right(num, angle):
    """Moves turtle num times forward and face right"""
    for _ in range(num):
        timmy.forward(100)
        timmy.right(angle)

def dashed_line(num):
    """Moving the turtle forward with a trailing dashed line"""
    for _ in range(num):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

def random_color():
    """Chooses a random pen color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r,g,b)

def draw_shapes(list):
    """Move the turtle to create polygons with random pen color"""
    for item in list:
        n = item
        angle = 360/item
        random_color()
        forward_right(n, angle)

def random_walk(steps):
    for _ in range(steps):
        random_color()
        timmy.forward(30)
        direction = random.choice([timmy.right, timmy.left])
        direction(90)

def draw_spirograph(size, angle):
    total_angle = 0
    while total_angle < 360:
        random_color()
        timmy.setheading(total_angle)
        timmy.circle(size)
        total_angle += angle

# list = [i for i in range(3,10)]
# draw_shapes(list)

# random_walk(1000)

draw_spirograph(100,5)
# Displaying Turtle in a window
screen.exitonclick()