from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SPEED = 20


class Game:
    def __init__(self):
        self.size = []
        self.create_snake()
        self.head = self.size[0]

    def create_snake(self):
        for position in START_POS:
            self.longer_snake(position)

    def longer_snake(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.size.append(snake)

    def extendo(self):
        self.longer_snake(self.size[-1].position())

    def move(self):

        for snake_body in range(len(self.size) - 1, 0, -1):
            x_cor = self.size[snake_body - 1].xcor()
            y_cor = self.size[snake_body - 1].ycor()
            self.size[snake_body].goto(x=x_cor, y=y_cor)

        self.head.forward(SNAKE_SPEED)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
