from turtle import Turtle

class Snake:

    def __init__(self):
        self.color = 'white'
        self.shape = 'square'
        self.length = 3
        self.snake = []

        xcor = 0
        for i in range(0, self.length):
            segment = Turtle(self.shape)
            segment.color(self.color)
            segment.penup()
            segment.setx(xcor)
            self.snake.append(segment)
            xcor -= 20


    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            pos_prev = self.snake[i - 1].position()
            self.snake[i].goto(pos_prev)
