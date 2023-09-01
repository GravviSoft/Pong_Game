from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def move_pad_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def move_pad_dn(self):
        # for l in self.lft_pd_instances:
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)


    # def left_paddle(self):
    #     y_cor = 240
    #     t = Turtle()
    #     t.shape("square")
    #     t.color("white")
    #     t.shapesize(5, 1)
    #     t.penup()
    #     t.speed("fastest")
    #     t.goto(-430, y_cor)
    #     y_cor -= 20
    #     self.lft_pd_instances.append(t)
    #
    # def right_paddle(self):
    #     y_cor = 240
    #     t = Turtle()
    #     t.shape("square")
    #     t.color("white")
    #     t.shapesize(5, 1)
    #     t.penup()
    #     t.speed("fastest")
    #     t.goto(420, y_cor)
    #     y_cor -= 20
    #     self.rt_pd_instances.append(t)

    # def move_r_pad_up(self):
    #     # for l in self.rt_pd_instances:
    #     new_y_cor = self.rt_pd_instances[0].ycor() + 20
    #     self.rt_pd_instances[0].goto(420, new_y_cor)
    #
    # def move_r_pad_dn(self):
    #     # for l in self.rt_pd_instances:
    #     new_y_cor = self.rt_pd_instances[0].ycor() - 20
    #     self.rt_pd_instances[0].goto(420, new_y_cor)
