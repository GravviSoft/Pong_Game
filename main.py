import random
import time
from turtle import Turtle, Screen
from background import Background
from paddles import Paddle
from ball import Ball
from score import ScoreBoard

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

background = Background()
l_paddle = Paddle((-430, 240))
r_paddle = Paddle((420, 240))
ball = Ball()
score = ScoreBoard()


screen.listen()
# screen.update()
screen.onkey(key="a", fun=l_paddle.move_pad_up)
screen.onkey(key="z", fun=l_paddle.move_pad_dn)
screen.onkey(key="Up", fun=r_paddle.move_pad_up)
screen.onkey(key="Down", fun=r_paddle.move_pad_dn)

ball_facing_right = True
hit_wall = False

while not hit_wall:
    time.sleep(.07)
    screen.update()
    ball.move_ball()

    #if hit right paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 250:
        ball.move_ball_left()
        ball_facing_right = False
        score.right_scored()

    #if hit left paddle
    if ball.distance(l_paddle) < 40 and ball.xcor() < 250:
        ball.move_ball_right()
        ball_facing_right = True
        score.left_scored()

    # # if hit left wall or right wall.
    if ball.xcor() < -450 or ball.xcor() > 440:
        hit_wall = True

    #if ball is facing right and hits the bottom of screen - move ball top right corner
    if ball_facing_right and ball.ycor() < -290:
        ball.move_ball_top_right()

    #if ball is facing right and hits the top of screen - move ball bottom right corner
    if ball_facing_right and ball.ycor() > 295:
        ball.move_ball_bottom_right()

    #if ball is facing left and hits the bottom of screen - move ball top left corner
    if not ball_facing_right and ball.ycor() < -290:
        ball.move_ball_top_left()

    #if ball is facing left and hits the top of screen - move ball bottom left corner
    if not ball_facing_right and ball.ycor() > 295:
        ball.move_ball_bottom_left()

screen.exitonclick()
