from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


my_snake = Snake()
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




























screen.exitonclick()