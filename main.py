from turtle import Screen, Turtle
import time
from frog import Frog
from level import Level
from larusso_autos import Auto

traffic_speed = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)
screen.register_shape("frog.gif")
frog = Frog()
level = Level()
screen.listen()
carmaker = Auto()
screen.onkeypress(frog.move_up, "w")
screen.onkeypress(frog.move_down, "s")
screen.onkeypress(frog.move_left, "a")
screen.onkeypress(frog.move_right, "d")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(traffic_speed)

    if frog.ycor() > 280:
        level.level_up()
        frog.reset_position()
        traffic_speed *= 0.9

    carmaker.create_auto()

    for car in carmaker.showroom:
        car.forward(5)
        if car.distance(frog) < 20:
            game_is_on = False


















screen.exitonclick()