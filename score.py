from turtle import Turtle

FONT = ('arial', 90, 'normal')


class ScoreBoard:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        self.left_scoreboard_instance = []
        self.right_scoreboard_instance = []
        self.left_scoreboard()
        self.right_scoreboard()

    def left_scoreboard(self):
        turtle = Turtle()
        turtle.color("white")
        turtle.penup()
        turtle.hideturtle()
        turtle.goto((-140, 190))
        turtle.write(arg=self.left_score, align='left', font=FONT)
        self.left_scoreboard_instance.append(turtle)

    def right_scoreboard(self):
        turtle = Turtle()
        turtle.color("white")
        turtle.penup()
        turtle.hideturtle()
        turtle.goto((90, 190))
        turtle.write(arg=self.right_score, align='left', font=FONT)
        self.right_scoreboard_instance.append(turtle)

    def left_scored(self):
        self.left_score += 1
        self.left_scoreboard_instance[-1].clear()
        self.left_scoreboard()

    def right_scored(self):
        self.right_score += 1
        self.right_scoreboard_instance[-1].clear()
        self.right_scoreboard()