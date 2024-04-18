from turtle import Turtle,Screen
import time

POSITIONS=[(-10,0),(0,0),(10,0)]
UNIT_MOVE=10

class Snake:
    def __init__(self):
        self.body=[]
        self.create_snake()
        self.head=self.body[0]

    def create_snake(self):
        for i in range(len(POSITIONS)):
            a=Turtle("square")
            a.penup()
            a.color("white")
            a.goto(POSITIONS[i])
            self.body.append(a)

    def move(self):
        for i in range(len(self.body)-1,0,-1):
            p=self.body[i-1].xcor()
            q=self.body[i-1].ycor()
            self.body[i].goto(p,q)
        self.body[0].forward(UNIT_MOVE)
    
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)

