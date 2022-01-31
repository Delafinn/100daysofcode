import turtle
from turtle import Turtle
from turtle import Screen

STARTING_POSITIONS = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    # initialize the snake

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    segments = []

    def create_snake(self):
        # creates segments of the snake using a for loop
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def add_segment(self,position):
        newsegment = Turtle("square")
        newsegment.penup()
        newsegment.clear()
        newsegment.color("white")
        newsegment.goto(position)
        self.segments.append(newsegment)


    # moves Snake
    def move(self):
        for seg_num in range(len(self.segments) -1 , 0, -1):
            newx = self.segments[seg_num - 1].xcor()
            newy = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newx,newy)
        self.head.fd(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
