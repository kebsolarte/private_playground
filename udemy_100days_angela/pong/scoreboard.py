from turtle import Turtle

TEXT_ALIGNMENT = 'center'
TEXT_FONT = ('Courier', 20, 'normal')
X_POS = 60
Y_POS = 260

class Scoreboard(Turtle):
    
    def __init__(self, side:str = 'right') -> None:
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.y_pos = Y_POS

        if side == 'left':
            self.x_pos = X_POS * -1
        else: self.x_pos = X_POS

        self.goto(self.x_pos, self.y_pos)
        self.print_score()


    def print_score(self) -> None:
        self.write(f"{self.score}", align=TEXT_ALIGNMENT, font=TEXT_FONT)

    
    def update_score(self) -> None:
        self.score += 1
        self.clear()
        self.print_score()

    
    



