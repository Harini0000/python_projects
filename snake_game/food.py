from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_wid=0.7,stretch_len=0.7)
        self.color("red")
        self.speed("fastest")
        self.spawn()


    def spawn(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
