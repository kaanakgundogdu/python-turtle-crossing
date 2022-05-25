from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.CREATED_CARS = []
        self.car_speed = 1
        for i in range(20):
            self.create_car()

    def create_car(self):
        self.car = Turtle()
        self.car.shapesize(1, 2)
        self.car.shape('square')
        self.car.penup()
        self.go_random_pos(self.car)
        self.car.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.CREATED_CARS.append(self.car)

    def go_random_pos(self, car):
        random_x = random.randint(0, 500)
        random_y = random.randint(-250, 250)
        car.goto(300 + random_x, random_y)

    def move_cars(self):
        for i in self.CREATED_CARS:
            if i.xcor() < -305:
                self.go_random_pos(i)
            old_x = i.xcor()
            i.goto(old_x - MOVE_INCREMENT * self.car_speed, i.ycor())
