''' main Pyfrog '''
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("black")

player1 = Player()
car_manager = CarManager()
scoreboard = Scoreboard((-270,270))

screen.colormode(255)
screen.onkeypress(fun = player1.go_up, key = "Up")
screen.onkeypress(fun = player1.go_right, key = "Right")
screen.onkeypress(fun = player1.go_left, key = "Left")

GAME_IS_ON = True
while GAME_IS_ON:


    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    if player1.ycor() > 280:
        player1.round_end()
        scoreboard.increase_score()

    for car in car_manager.all_cars:
        if car.distance(player1) < 20:
            GAME_IS_ON = False
            scoreboard.game_over()



screen.exitonclick()

