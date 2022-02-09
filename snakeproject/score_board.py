from turtle import Turtle


class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.goto(0, 320)
        self.color("white")
        self.write(f"Score: {self.score} high_score: {self.high_score}", align = "center", font=("Arial", 15, "normal"))

    def update_SB(self):
        self.clear()
        self.write(f"Score: {self.score} high_score: {self.high_score}" , align = "center", font=("Arial", 15, "normal"))


    def Increase_Score(self):
        self.score += 1
        self.update_SB()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as file:
                file.write(f" {self.high_score}")
        self.score = 0
        self.update_SB()
