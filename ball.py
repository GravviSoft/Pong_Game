import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.home()
        self.setheading(random.randrange(350, 390))

    def move_ball(self):
        self.fd(20)

    def move_ball_left(self):
        num = random.randint(150, 210)
        self.setheading(num)
        self.fd(20)

    def move_ball_right(self):
        num = random.randrange(330, 420)
        self.setheading(num)
        self.fd(20)

    def move_ball_top_right(self):
        num = random.randint(25, 75)
        self.setheading(num)
        self.fd(20)

    def move_ball_top_left(self):
        num = random.randint(115, 165)
        self.setheading(num)
        self.fd(20)

    def move_ball_bottom_right(self):
        num = random.randint(290, 345)
        self.setheading(num)
        self.fd(20)

    def move_ball_bottom_left(self):
        num = random.randint(205, 255)
        self.setheading(num)
        self.fd(20)