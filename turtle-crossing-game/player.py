from turtle import Turtle
import scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.finish_line_y=FINISH_LINE_Y
        self.shape('turtle')
        self.color('black')
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        old_y = self.ycor()
        self.goto(0, old_y + MOVE_DISTANCE)


    def complete_level(self):
        self.goto(STARTING_POSITION)
