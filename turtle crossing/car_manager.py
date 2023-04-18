''' car manager class creation'''
from turtle import Turtle
import random


COLORS = ["yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LEFT = 180

class CarManager(Turtle):
    '''defining the cars in game'''

    def __init__(self):
        '''Initialize Cars'''
        super().__init__()
        self.all_cars = []

    def create_car(self):
        '''creating the cars in the game'''
        random_chance = random.randint(1,5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid = 1, stretch_len = 1)
            new_car.penup()
            new_car.clear()
            new_car.color(random.choice(COLORS))
            random_y_point = random.randint(-251,251)
            new_car.goto(300, random_y_point)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_car(self):
        '''moving the cars in the game'''
        random_y_point = random.randint(-251,251)
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)
            if car.xcor() < -290:
                car.goto(300,random_y_point)
