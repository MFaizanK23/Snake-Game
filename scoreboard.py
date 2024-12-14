from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write("Score = 0", align="center", font=('Arial', 18, 'normal'))

    def add_points(self):
        self.clear()
        self.points += 1
        self.write(f"Score = {self.points}", align="center", font=('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 24, 'normal'))