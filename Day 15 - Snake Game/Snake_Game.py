from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('The Snake Game')
screen.tracer(0)
x = 0

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food,
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.refresh()

    #Detect collision with wall
    if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() > 295 or snake.segments[0].ycor() < -295:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
