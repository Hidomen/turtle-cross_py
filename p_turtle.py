from turtle import Turtle

class Turtle(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.pu()
        self.goto(0,-250)
        self.setheading(90)
        # self.color("black")

        pass
    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)