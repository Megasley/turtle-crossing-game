from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def refresh_score(self):
        self.clear()
        self.level = self.level + 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)