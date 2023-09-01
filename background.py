from turtle import Turtle, Screen
CENTER_COURT = [(0, 280), (0, 240), (0, 200), (0, 160), (0, 120), (0, 80), (0, 40), (0, 0), (0, -40), (0, -80), (0, -120),
           (0, -160), (0, -200), (0, -240), (0, -280)]

class Background:

    def __init__(self):
        self.make_court()

    def make_court(self):
        for x in CENTER_COURT:
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.shapesize(stretch_wid=1, stretch_len=0.3)
            t.speed("fastest")
            t.goto(x)
