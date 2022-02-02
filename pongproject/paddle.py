'''Creating a Paddle Class '''
from turtle import Turtle
MOVE_DISTANCE = 25
UP = 90


class Paddle(Turtle):
    '''Making a Paddle class for each player '''

    def __init__(self,position):
        '''Initialize paddles'''
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.clear()
        self.goto(position)
        self.setheading(UP)
        self.speed("fastest")
        self.shapesize(stretch_wid = 1, stretch_len = 5,)



    def go_up(self):
        ''' function to have the paddle go up'''
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)


    def go_down(self):
        ''' function to have the paddle go down'''
        new_ycor = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor)
