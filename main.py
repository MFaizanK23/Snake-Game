from turtle import Turtle, Screen
import time
from snake_game import Game
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Game()
meal = Food()
score = Scoreboard()

# direction controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(meal) < 15:
        meal.refresh()
        score.add_points()
        snake.extendo()

    # detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_running = False
        score.game_over()

    #detect collision with tail
    for segment in snake.size[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            score.game_over()


screen.exitonclick()
