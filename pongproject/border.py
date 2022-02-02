'''Creation of the border in Pong'''
from turtle import Turtle

class Border(Turtle):
    '''Border class'''

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.clear()
        self.hideturtle()
        self.goto(400,280)
        self.pendown()
        self.goto(-400,280)
        self.penup()
        self.goto(400,-280)
        self.pendown()
        self.goto(-400,-280)
