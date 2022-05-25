import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_man = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkeypress(player.move_turtle, 'Up')

screen.listen()

game_is_on = True
can_cars_move: True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_man.move_cars()
    for i in car_man.CREATED_CARS:
        if player.distance(i.xcor(), i.ycor()) < 20:
            scoreboard.game_over()
            time.sleep(10)


    if player.ycor() > player.finish_line_y:
        player.complete_level()
        scoreboard.update_level()
