from turtle import Turtle


class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 320)
        self.color("white")
        self.write(f"Score: {self.score} ", align = "center", font=("Arial", 15, "normal"))

    def update_SB(self):
        self.clear()
        self.write(f"Score: {self.score} " , align = "center", font=("Arial", 15, "normal"))


    def Increase_Score(self):
        self.score += 1
        self.update_SB()



    def Game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(" Gameover!", align = "center", font=("Arial", 32, "normal"))
