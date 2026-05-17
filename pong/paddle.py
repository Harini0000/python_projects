from turtle import Screen, Turtle

class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.up()
        self.goto(location)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > - 240:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
