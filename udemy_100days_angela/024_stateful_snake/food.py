from turtle import Turtle
import random

class Food(Turtle):
    """
    Class to instantiate the food of the snake.
    """

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.refresh()
        
    
    def refresh(self) -> None:
        """
        Method to refresh the location of the food.
        """
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)   # y set to 260 to give way for the scoreboard
        self.goto(x, y)
