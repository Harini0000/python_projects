from turtle import Screen,Turtle
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

# ---------------- SCREEN SETUP ---------------- #

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor((112,92,75))
screen.title("My Snake Game")
screen.tracer(0)

# ---------------- DRAW BORDER ---------------- #

border = Turtle()
border.hideturtle()
border.color("black")
border.width(10)
border.penup()
border.goto(-290, -290)
border.pendown()
border.pensize(3)

for _ in range(4):
    border.forward(580)
    border.left(90)

# ---------------- GAME OBJECTS ---------------- #

snake = Snake()
food = Food()
score = Scoreboard()

# ---------------- CONTROLS ---------------- #

def setup_controls():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

setup_controls()

# ---------------- START GAME ---------------- #

answer = screen.textinput(
    title="Important Question!",
    prompt="Do you wanna play a snake game like in the old nokia phones? (y/n)"
)

play = answer and answer.lower() == "y"

if play:
    name = screen.textinput(
        title="Snake Game",
        prompt="What is your name?"
    )
setup_controls()
# ---------------- MAIN GAME LOOP ---------------- #

while play:

    game_is_on = True

    while game_is_on:

        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.spawn()
            score.update_score()
            snake.extend()

        # Detect collision with wall
        if (
            snake.head.xcor() > 290
            or snake.head.xcor() < -290
            or snake.head.ycor() > 290
            or snake.head.ycor() < -290
        ):
            game_is_on = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False

        # Game over handling
        if not game_is_on:

            score.game_over()
            score.highscore(name)

            answer = screen.textinput(
                title="Game Over",
                prompt="Do you wanna play again? (y/n)"
            )

            play = answer and answer.lower() == "y"

            if play:

                # Remove old snake from screen
                for segment in snake.segments:
                    segment.goto(1000, 1000)

                # Create fresh snake
                snake = Snake()

                # Reset controls to new snake
                setup_controls()

                # Reset score
                score.score = 0
                score.update_scoreboard()

                # Respawn food
                food.spawn()

screen.exitonclick()