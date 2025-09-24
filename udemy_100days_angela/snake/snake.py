from turtle import Turtle

class Snake:

    def __init__(self):
        self.color = 'white'
        self.shape = 'square'
        self.length = 3
        self.snake = []





    def move():






snake_color = 'white'
snake_shape = 'square'

xcor = 0
snake = []
for i in range(0,3):
    block = Turtle(snake_shape)
    block.color(snake_color)
    block.penup()
    block.setx(xcor)
    snake.append(block)
    xcor -= 20


game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    
    for i in range(len(snake) - 1, 0, -1):
        pos_prev = snake[i - 1].position()
        snake[i].goto(pos_prev)

    snake[0].forward(20)
