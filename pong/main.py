from turtle import Screen,Turtle
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

# ---------------- DRAW BORDER ---------------- #

border = Turtle()
border.hideturtle()
border.color("white")
border.penup()
border.goto(-400, -300)
border.pendown()
border.pensize(3)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.penup()
border.goto(0, 300)
border.setheading(270)
while border.ycor() > -300:
    border.pendown()
    border.forward(10)
    border.penup()
    border.forward(10)


l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    #detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()