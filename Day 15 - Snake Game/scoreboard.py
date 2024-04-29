from turtle import Turtle
import pandas as pd
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.high_score = 0
        self.read_highscore()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.read_highscore()}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.update_scoreboard()

    def save_highscore(self):
        with open("high_score", mode="w") as file:
            file.write(f'{self.high_score}')

    def read_highscore(self):
        with open("high_score", mode="r") as file:
            contents = file.read()
            return contents

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.high_score()

    # def high_score(self):
    #     self.goto(0, 260)
    #     self.write(f"High Score: {self.score}", align=ALIGNMENT, font=FONT)
