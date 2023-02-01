from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1.1)
        self.color("white")
        self.penup()
        self.speed(1)
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit_paddle(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)

