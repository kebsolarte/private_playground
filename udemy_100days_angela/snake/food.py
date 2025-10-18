from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.refresh()
        
        
    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
