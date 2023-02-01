from turtle import Turtle


class Paddles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.resizemode("user")
        self.shape("square")
        self.shapesize(1, 3, 1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.back(20)








