from turtle import Turtle, Screen
import random
import tkinter.messagebox as msg

# Setting the screen object state
screen = Screen()
screen.title("Turtle Race!")
screen.setup(width=600, height=600)

# Asking for user input via popup
user_bet = screen.textinput(title="Choose your turtle!", prompt="Which turtle do you think would win the race (ROYGBV)?").lower()

# Setting the turtle colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

# Creating the turtle object instances and saving them in a list
x = -280
y = -250
turtles = []
for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.speed(7)
    turtle.goto(x=x, y=y)
    turtles.append(turtle)
    y += 100

# Main game logic
game_over = False
while not game_over:
    # Sets the forward movement randomly
    for turtle in turtles:
        turtle.forward(random.randint(1,20))

        # Check if the turtle crosses the finish line and prints the results in a msg popup
        if turtle.xcor() >= 280:
            if turtle.pencolor() == user_bet:
                msg.showinfo("Race finished!", f"The {turtle.pencolor()} turtle won the race! You won!")
            else:
                msg.showinfo("Race finished!", f"The {turtle.pencolor()} turtle won the race! You lost.")

            game_over = True

screen.exitonclick()