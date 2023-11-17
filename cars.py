from turtle import Turtle
import random

colors = ["green", "red", "blue", "orange", "yellow", "black", "brown"] # more and more


class Cars(Turtle):
    def __init__(self):
        super().__init__()

        spawn_point = random.randint(-200,250)

        self.color(random.choice(colors))
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=0.7),
        self.pu()

        self.goto(350,spawn_point)
        self.setheading(180)

    def move(self, level):
        if not self.xcor() < -350: 
            self.forward(random.randint(round(10 + 1.1*level), round(20 + 1.1*level)))

        