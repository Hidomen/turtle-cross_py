from turtle import Turtle

FONT = ("Courier", 12, "bold")

class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-200,250)
        
        self.update()

    def update(self):
        self.write(f"Level : {self.level}", align="center", font=FONT)

    
    def level_up(self):
        self.level += 1

        self.clear()
        self.update()


    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\n your score was {self.level}", align="center", font=("Courier", 36, "bold"))