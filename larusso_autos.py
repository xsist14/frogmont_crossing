from turtle import Turtle
import random

class Auto(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.showroom = []


    def drive(self):
        self.forward(1)



    def create_auto(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_position = random.randint(-270, 270)
            new_car.penup()
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            new_car.color((r, g, b))
            new_car.setheading(180)
            new_car.goto(300, y_position)
            self.showroom.append(new_car)

