from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.up()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(align=ALIGNMENT, font=FONT, arg=self.score_l)
        self.goto(100, 200)
        self.write(align=ALIGNMENT, font=FONT, arg=self.score_r)

    def l_win(self):
        self.score_l += 1
        self.update_scoreboard()

    def r_win(self):
        self.score_r += 1
        self.update_scoreboard()

