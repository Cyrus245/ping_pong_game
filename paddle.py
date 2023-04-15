from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=6)
        self.penup()
        self.shape('square')
        self.coordinate = coordinate
        self.paddle_direction()

    def paddle_direction(self):
        self.goto(self.coordinate)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
