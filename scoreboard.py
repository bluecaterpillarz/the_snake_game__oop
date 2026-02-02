from turtle import Turtle

FONT=("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(-5,270)
        self.penup()
        self.score_refresh()
    def score_refresh(self):
        self.clear()
        self.write(f"Score:{self.score}",align="center",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=FONT)

