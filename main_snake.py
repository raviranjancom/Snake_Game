from turtle import Turtle,Screen
import time
from snake import Snake

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_on=True

snake=Snake()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

while game_on==True:
    screen.update()
    time.sleep(0.05)
    snake.move()

screen.exitonclick()
