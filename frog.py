from turtle import Turtle
FROG_SPEED = 20
HOME_POSITION = (0, -270)

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("frog.gif")
        self.penup()
        self.reset_position()

    def reset_position(self):
        self.goto(HOME_POSITION)


    def move_up(self):
        self.setheading(90)
        self.forward(FROG_SPEED)

    def move_down(self):
        self.setheading(270)
        self.forward(FROG_SPEED)

    def move_left(self):
        self.setheading(180)
        self.forward(FROG_SPEED)

    def move_right(self):
        self.setheading(0)
        self.forward(FROG_SPEED)