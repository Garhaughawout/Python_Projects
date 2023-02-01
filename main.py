from turtle import Screen
from paddles import Paddles
from scoreboard import Scoreboard
from ball import Ball
import time

game_is_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
scoreboard = Scoreboard()
ball = Ball()
r_paddle = Paddles((360, 0))
l_paddle = Paddles((-360, 0))


screen.listen()
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")


while game_is_on:
    screen.update()
    time.sleep(.07)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.xcor() < -390:
        scoreboard.score_2 += 1
        scoreboard.change_score()
        ball.reset()
    if ball.xcor() > 390:
        scoreboard.score_1 += 1
        scoreboard.change_score()
        ball.reset()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 20 and ball.xcor() < -340:
        ball.hit_paddle()
    if scoreboard.score_1 == 5:
        game_is_on = False
        print("Player 1 has won!!")
    if scoreboard.score_2 == 5:
        game_is_on = False
        print("Player 2 has won!!")


screen.exitonclick()
