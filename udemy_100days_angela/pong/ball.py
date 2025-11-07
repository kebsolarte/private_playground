from turtle import Turtle
import random

BALL_WIDTH = 1
BALL_HEIGHT = 1
X_POS_START = 0
Y_POS_START = 0
BALL_SPEED = 15
SENSITIVITY = 50

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=BALL_WIDTH, stretch_len=BALL_HEIGHT)
        self.x_increment = BALL_SPEED
        self.y_increment = BALL_SPEED

        self.create_ball()

    
    def create_ball(self) -> None:
        self.goto(X_POS_START, Y_POS_START)


    def move(self) -> None:
        new_x = self.xcor() + self.x_increment
        new_y = self.ycor() + self.y_increment
        self.goto(new_x, new_y)

    
    def bounce_y(self) -> None:
        self.y_increment *= -1

    
    def bounce_x(self) -> None:
        self.x_increment *= -1


    def is_ball_on_paddle(self, paddle) -> bool:
        if abs(self.xcor()) >= (abs(paddle.xcor()) - 20):
            return True
        
    
    def is_ball_out_of_bounds(self) -> bool:
        if abs(self.xcor()) >= 380:
            return True
    

    def is_ball_hit(self, paddle) -> bool:
        if self.distance(paddle) < SENSITIVITY and self.is_ball_on_paddle(paddle):
            return True
        

    def reset_position(self) -> None:
        self.create_ball()
        self.x_increment = BALL_SPEED
        self.y_increment = BALL_SPEED
        self.y_increment *= random.choice([1,-1])
        self.bounce_x()


    def increase_speed(self) -> None:
        self.x_increment *= 1.1
        
    

    


    
    