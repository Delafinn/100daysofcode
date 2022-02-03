'''main pong program'''
import time
from turtle import Screen
from paddle import Paddle
from border import Border
from ball import Ball
from score import Score


screen = Screen()
screen.title("PongPy")
screen.setup(width=800, height=620)
screen.bgcolor("black")
screen.tracer(0)

border = Border()
ball = Ball()
scorer = Score((50,290))
scorel = Score((-50,290))
RIGHT_PADDLE = Paddle((350,0))
LEFT_PADDLE = Paddle((-350,0))


screen.listen()
screen.onkeypress(fun = RIGHT_PADDLE.go_up,key ="Up")
screen.onkeypress(fun = RIGHT_PADDLE.go_down,key = "Down")
screen.onkeypress(fun = LEFT_PADDLE.go_up,key = "w")
screen.onkeypress(fun = LEFT_PADDLE.go_down,key = "s")


RUN_PROGRAM = True
#  main program loop
while RUN_PROGRAM is True:
    screen.update()
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.y_bounce()
    elif ball.distance(RIGHT_PADDLE) < 50 or ball.distance(LEFT_PADDLE) < 50:
        ball.x_bounce()
    elif ball.xcor() > 370:
        time.sleep(1)
        ball.update()
        scorel.increase_score()
    elif ball.xcor() < -370:
        time.sleep(1)
        ball.update()
        scorer.increase_score()
    elif scorer.score == 5 or scorel.score ==5:
        RUN_PROGRAM = False

scorer.game_over()
screen.exitonclick()
