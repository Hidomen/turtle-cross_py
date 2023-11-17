from turtle import Screen
from cars import Cars
from p_turtle import Turtle
from level_board import LevelBoard
import time

WIDTH = 600
HEIGHT = 600

FINISH_LINE = 250

def game():
    screen = Screen()
    turtle = Turtle()
    levelboard = LevelBoard()
    cars = []
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.tracer(0)


    game_over = False


    screen.listen()
    screen.onkey(turtle.up, "w")
    screen.onkey(turtle.down, "s")

    spawn_number = 0
    anti_difficulty = 10

    while not game_over:
        
        time.sleep(0.1)
        spawn_number += 1
        screen.update()
        
        for i in range(len(cars)):
            cars[i].move()
            # collision detect
            if turtle.distance(cars[i]) < 20:
                levelboard.gameover()
                game_over = True

        if not spawn_number % anti_difficulty:
            cars.append(Cars())


        if turtle.ycor() > FINISH_LINE:
            levelboard.level_up()
            anti_difficulty -= 1
            turtle.reset()

    screen.exitonclick()


game()