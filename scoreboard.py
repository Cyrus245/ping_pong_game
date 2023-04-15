from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(f"player1:{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"player2:{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_pont(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
