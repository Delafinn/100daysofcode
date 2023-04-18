'''scoreboard class'''
from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    '''defining the scoreboard in game'''

    def __init__(self, position):
        super().__init__()
        self.score = 1
        self.color("white")
        self.penup()
        self.clear()
        self.goto(position)
        self.hideturtle()
        self.write(f"Level: {self.score} ", align = "left", font=(FONT))

    def update_sb(self):
        '''updates the scoreboard with clear and then writes the new score'''
        self.clear()
        self.write(f"Level: {self.score} " , align = "left", font=(FONT))


    def increase_score(self):
        '''adds a 1 to the score then calls the update_scoreboard method'''
        self.score += 1
        self.update_sb()


    def game_over(self):
        '''adds the gameover banner above the ball at end game'''
        self.goto(0,50)
        self.color("white")
        self.write("Gameover!", align = "center", font=(FONT))
