from turtle import Turtle

# Constants
STARTING_X_POSITION = 0
MOVE_DISTANCE =20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    """
    Class to instantiate and manage the snake object in the game.
    """

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self) -> None:
        """
        Creates the first three segments of the snake.
        """
        xcor = STARTING_X_POSITION
        for i in range(0, 3):
            self.add_segment((xcor,0))
            xcor -= 20


    def add_segment(self, position) -> None:
        """
        Creates a new snake segment.
        """
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)


    def extend(self) -> None:
        """
        Extends the snake once it catches the food.
        """        
        last_segment_position = self.segments[-1].position()
        self.add_segment(last_segment_position)


    def move(self) -> None:
        """
        Initiates a forward cascading movement of the snake segments.
        """
        for i in range(len(self.segments) - 1, 0, -1):
            pos_prev = self.segments[i - 1].position()
            self.segments[i].goto(pos_prev)

        self.head.forward(MOVE_DISTANCE)


    def up(self) -> None:
        """
        Make the snake face up.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self) -> None:
        """
        Make the snake face down.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    
    def left(self) -> None:
        """
        Make the snake face left.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    
    def right(self) -> None:
        """
        Make the snake face right.
        """
        if self.head.heading() != LEFT:    
            self.head.setheading(RIGHT)