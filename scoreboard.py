from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.scoreboard = Turtle()
        self.score_1 = 0
        self.score_2 = 0
        self.border = Turtle()
        self.write_score()
        self.create_border()

    def write_score(self):
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.color("white")
        self.scoreboard.goto(x=0, y=225)
        self.scoreboard.write(f"{self.score_1}            {self.score_2}", align="center", font=("Arial", 40,"bold"))

    def change_score(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"{self.score_1}            {self.score_2}", align="center", font=("Arial", 40, "bold"))

    def create_border(self):
        self.border.goto(x=0, y=-280)
        self.border.pencolor("white")
        self.border.pensize(5)
        self.border.setheading(90)
        self.border.hideturtle()
        for lines in range(1, 13):
            self.border.forward(25)
            self.border.penup()
            self.border.forward(25)
            self.border.pendown()




