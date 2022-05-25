from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_GAME_OVER = ("Courier", 32, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.penup()
        self.goto(-230, 250)
        self.color('black')
        self.write(f"Level:{self.level}", False, font=FONT, align='center')
        self.hideturtle()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level:{self.level}", False, font=FONT, align='center')

    def game_over(self):
        self.clear()
        self.goto(0, 0)

        self.write(f"GAME OVER", False, font=FONT_GAME_OVER, align='center')
