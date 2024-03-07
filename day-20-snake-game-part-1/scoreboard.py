from turtle import Turtle
# avoid hardcode in variables, easy to change later

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("data.txt", mode="r") as f:
            self.high_score = int(f.read())
        self.hideturtle()
        self.penup()
        self.goto(-20, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(align=ALIGNMENT, font=FONT, arg=f"Score: {self.score} High Score: {self.high_score}")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def eat(self):
        self.score += 1
        self.update_scoreboard()



