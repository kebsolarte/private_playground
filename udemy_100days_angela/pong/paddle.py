from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
X_POS = 350
Y_POS = 0

class Paddle(Turtle):
    
    def __init__(self, side:str = 'right') -> None:
        super().__init__()
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.side = side
        self.penup()
        self.color('white')
        self.shape('square')
        # self.shapesize(stretch_wid=self.width, stretch_len=self.height)
        self.y_pos = Y_POS

        if self.side == 'left':
            self.x_pos = X_POS * -1
        else: self.x_pos = X_POS

        self.create_paddle()

        
    def create_paddle(self) -> None:
        self.goto(self.x_pos, self.y_pos)

    
    def move_up(self) -> None:
        self.y_pos += 20
        self.goto(self.x_pos, self.y_pos)

    
    def move_down(self) -> None:
        self.y_pos -= 20
        self.goto(self.x_pos, self.y_pos)
   
        

