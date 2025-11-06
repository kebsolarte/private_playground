from turtle import Screen
from paddle import Paddle


# Set the screen attributes
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Initialize paddle
left_paddle = Paddle(side='left')
right_paddle = Paddle(side='right')

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
    screen.update()









screen.exitonclick()