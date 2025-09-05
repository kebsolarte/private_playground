from turtle import Turtle, Screen

# Creating a Turtle object
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSlateGray4")

# Moving the Turtle
def forward_right(num):
    """Moves turtle num times forward and face right"""
    for _ in range(num):
        timmy.forward(100)
        timmy.right(90)

def dashed_line(num):
    """Moving the turtle forward with a trailing dashed line"""
    for _ in range(num):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

dashed_line(10)






# Displaying Turtle in a window
screen = Screen()
screen.exitonclick()