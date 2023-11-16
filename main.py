from turtle import Screen
from cars import Cars
from p_turtle import Turtle
import time


def game():
    screen = Screen()
    turtle = Turtle()
    cars = []
    # cars = Cars()
    screen.setup(width=600, height=600)
    screen.tracer(0)


    game_over = False


    screen.listen()
    screen.onkey(turtle.up, "w")
    screen.onkey(turtle.down, "s")

    spawn_number = 0
    difficulty = 5

    while not game_over:
        
        time.sleep(0.1)
        spawn_number += 1
        screen.update()
        
        for i in range(len(cars)):
            cars[i].move()
            # collision detect
            if turtle.distance(cars[i]) < 20:
                game_over = True

        if not spawn_number % difficulty:
            cars.append(Cars())


        if turtle.ycor() > 250:
            game_over = True
            print("you won")
    screen.exitonclick()


game()