'''This module is meant to track the score of the pong game'''
from turtle import Turtle

class Score(Turtle):
    ''' Score class with some attributes and methods'''

    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.clear()
        self.goto(position)
        self.hideturtle()
        self.write(f"Score: {self.score} ", align = "center", font=("Arial", 15, "normal"))

    def update_sb(self):
        '''updates the scoreboard with clear and then writes the new score'''
        self.clear()
        self.write(f"Score: {self.score} " , align = "center", font=("Arial", 15, "normal"))


    def increase_score(self):
        '''adds a 1 to the score then calls the update_scoreboard method'''
        self.score += 1
        self.update_sb()


    def game_over(self):
        '''adds the gameover banner above the ball at end game'''
        self.goto(0,50)
        self.color("white")
        self.write("Gameover!", align = "center", font=("Arial", 32, "normal"))
