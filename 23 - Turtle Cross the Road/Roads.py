import random
from turtle import *

INITIAL_SPEED = -10
MOVE_INCREMENT = -10

colors = ["green","yellow","black","blue","red","purple"]


class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = INITIAL_SPEED

    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=2, stretch_len=1)
            new_car.tiltangle(90)
            new_car.penup()
            new_car.car_speed = INITIAL_SPEED
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT