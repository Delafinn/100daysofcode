
import turtle
from turtle import Screen
import time
from food import Food
from snake import *
from score_board import Score_Board


'''' Create a screen'''


scr = Screen()
scr.title("Snake")
scr.setup(width=640, height=720)
scr.bgcolor("black")
scr.tracer(0)

sb = Score_Board()
snake = Snake()
food = Food()
border = Turtle()
border.color("white")
border.penup()
border.clear()
border.hideturtle()
border.goto(300,300)
border.pendown()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)


''' listing for inputs to the screen '''
scr.listen()
scr.onkeypress(snake.up,"Up",)
scr.onkeypress(snake.down,"Down",)
scr.onkeypress(snake.right,"Right", )
scr.onkeypress(snake.left,"Left",)

''' while loop to keep the game running'''
GAME_IS_ON = True
while GAME_IS_ON:

    scr.update()
    time.sleep(0.15)
    snake.move()

    ''' detect collision with food '''
    if snake.head.distance(food) < 15:
        food.refresh()
        sb.Increase_Score()
        sb.update_SB()
        snake.extend()

    ''' detect collision with wall'''
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        GAME_IS_ON = False
        sb.Game_over()

    '''detect collision with self'''
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            GAME_IS_ON  = False
            sb.Game_over()

scr.exitonclick()


