from turtle import Turtle


class Paddle(Turtle):
    """determine where paddle going to (2 paddles)"""
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        """width = 20, default, height = 100, 5x20 default square 20"""
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y_position = self.ycor() + 20
        self.goto(self.xcor(), new_y_position)

    def go_down(self):
        new_y_position = self.ycor() - 20
        self.goto(self.xcor(), new_y_position)


