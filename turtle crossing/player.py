from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    ''' Creating the player '''

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.clear()
        self.setheading(UP)
        self.goto(STARTING_POSITION)

    def go_up(self):
        ''' function to have the paddle go up'''
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)

    def go_right(self):
        ''' function to have the paddle go right'''
        new_xcor = self.xcor() + MOVE_DISTANCE
        self.goto(new_xcor, self.ycor())

    def go_left(self):
        ''' function to have the paddle go left'''
        new_xcor = self.xcor() - MOVE_DISTANCE
        self.goto(new_xcor, self.ycor())

    def round_end(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
