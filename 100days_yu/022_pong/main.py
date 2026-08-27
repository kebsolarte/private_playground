from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the screen attributes
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Initialize objects
left_paddle = Paddle(side='left')
right_paddle = Paddle(side='right')
ball =Ball()
left_score = Scoreboard(side='left')
right_score = Scoreboard()

# Set keybindings
screen.listen()

# Left paddle
screen.onkeypress(fun=left_paddle.move_up, key='w')
screen.onkeypress(fun=left_paddle.move_down, key='s')

# Right paddle
screen.onkeypress(fun=right_paddle.move_up, key='Up')
screen.onkeypress(fun=right_paddle.move_down, key='Down')

# Main program
game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
 
    ball.move()

    # Detect collision with top and bottom walls
    if abs(ball.ycor()) >= 280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.is_ball_hit(left_paddle) or ball.is_ball_hit(right_paddle):
        ball.bounce_x()
        ball.increase_speed()


    # Detecting collision with right and left walls
    if ball.is_ball_out_of_bounds():
        if ball.xcor() > 0:
            left_score.update_score()
        else:
            right_score.update_score()

        ball.reset_position()
        

screen.exitonclick()