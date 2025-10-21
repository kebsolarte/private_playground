from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Sets the screen attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Instantiates the turtle objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Sets the keybindings for the snake object
screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")

# Main game program
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
  
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) == 300 or abs(snake.head.ycor()) > 290:
        game_over = True
        scoreboard.print_game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.print_game_over()


screen.exitonclick()
