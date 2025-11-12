from turtle import Turtle

# Constants
TEXT_ALIGNMENT = 'center'
TEXT_FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    """
    Class to instantiate a scoreboard.
    """

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.load_high_score()
        self.print_score()


    def print_score(self) -> None:
        """
        Prints the current score.
        """
        self.write(f"Score: {self.score} | Previous High Score: {self.high_score}", align=TEXT_ALIGNMENT, font=TEXT_FONT)

    
    def print_game_over(self) -> None:
        """
        Prints game over.
        """
        self.goto(0,0)
        self.write("GAME OVER!", align=TEXT_ALIGNMENT, font=TEXT_FONT)


    def load_high_score(self) -> None:
        """
        Checks and load high score.
        """
        try: 
            with open('high_score.txt', mode='r') as file:
                self.high_score = int(file.read())
        except:
            self.high_score = 0


    def save_score(self) -> None:
        """
        Checks if current score is higher than high score and save it.
        """

        if self.score > self.high_score:
            with open('high_score.txt', mode='w') as file:
                file.write(f"{self.score}")


    def update_score(self) -> None:
        """
        Increments the score by 1 and reprints the scoreboard.
        """
        self.score += 1
        self.clear()
        self.print_score()


   