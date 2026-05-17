from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Arial",24,"bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,290)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", align=ALLIGNMENT, font=FONT)


    def update_score(self):
        self.score += 1
        self.color("white")
        self.clear()
        self.update_scoreboard()

    def highscore(self, name):
        if self.score > self.high:
            self.high = self.score
        self.clear()
        self.goto(0,0)
        self.write(f"previous high_score: {self.high} by {name}", align=ALLIGNMENT, font=FONT)
