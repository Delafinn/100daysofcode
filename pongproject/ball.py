'''ball creation'''
from turtle import Turtle
import random
class Ball(Turtle):
    ''' creating the ball class'''


    def __init__(self,):
        super().__init__()
        MOVE_NUMS = [-4,-3,-2,2,3,4]
        self.color("white")
        self.shape("square")
        self.penup()
        self.clear()
        self.goto(0, 0)
        self.speed("slowest")
        self.ymove = random.choice(MOVE_NUMS)
        self.xmove = random.choice(MOVE_NUMS)
        self.shapesize(stretch_wid = 1, stretch_len = 1)

    def move(self):
        ''' creating the move function'''
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def y_bounce(self):
        '''changing the Y coordinates of the ball'''
        if self.ycor() > 300 or self.ycor() < -300:
            self.ymove *= -1

    def x_bounce(self):
        '''changing the X coordinates of the ball'''
        if self.xcor() > 350 or self.xcor() < -350:
            self.xmove *= -1.01

    def update(self):
        '''when a goal is scored the ball updates back to coordinates 0,0'''
        self.goto(0,0)
        self.move()
