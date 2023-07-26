from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.print_level()
    def level_up(self):
        self.level += 1

    def print_level(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-295, 260)
        self.write(f" Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

