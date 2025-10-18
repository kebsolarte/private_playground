from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Setting the snake attributes
snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")


game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.head.distance(food) < 20:
        print("Yummy!")
        food.refresh()



screen.exitonclick()
