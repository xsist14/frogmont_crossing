from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.num_level = 1
        self.color("black")
        self.goto(-270, 250)
        self.update_level_text()

    def level_up(self):
        self.num_level += 1
        self.update_level_text()

    def update_level_text(self):
        self.clear()
        self.write(f"Level: {self.num_level}", align="left", font=("Arial", 24, "normal"))
