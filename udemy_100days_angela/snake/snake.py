from turtle import Turtle

STARTING_POSITION = 0
MOVE_DISTANCE =20

class Snake:
    """
    Class to instantiate and manage the snake object in the game.
    """

    def __init__(self) -> None:
        self.segment = []
        self.create_snake()


    def create_snake(self) -> None:
        """
        Creates the first three segments of the snake.
        """

        xcor = STARTING_POSITION
        for i in range(0, 3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setx(xcor)
            self.segment.append(segment)
            xcor -= 20


    def move(self) -> None:
        """
        Initiates a forward cascading movement of the snake segments.
        """
        for i in range(len(self.segment) - 1, 0, -1):
            pos_prev = self.segment[i - 1].position()
            self.segment[i].goto(pos_prev)

        self.segment[0].forward(MOVE_DISTANCE)
