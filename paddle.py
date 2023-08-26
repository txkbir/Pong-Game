from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coord: tuple):
        super().__init__()
        self.speed('fastest')
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.coord = coord
        self.goto(self.coord)

    def up(self) -> None:
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self) -> None:
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def reset_paddle(self):
        self.goto(self.coord)
