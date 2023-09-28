from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


my_snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = 0

screen.listen()
screen.onkeypress(my_snake.up, "Up")
screen.onkeypress(my_snake.down, "Down")
screen.onkeypress(my_snake.left, "Left")
screen.onkeypress(my_snake.right, "Right")




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # detect collision with food

    if my_snake.head.distance(food) < 17:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

#     detect collision with wall
    if (my_snake.head.xcor() < -290 or my_snake.head.xcor() > 290
            or my_snake.head.ycor() < -290 or my_snake.head.ycor() > 290):
        game_is_on = False
        scoreboard.game_over()

# detect collision with tail
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



























screen.exitonclick()