import turtle
import time

import pandas
import pandas as pd

from pathlib import Path


ROOT = Path(__file__).resolve().parent

screen = turtle.Screen()
screen.title("U.S. States Game")
image = f"{ROOT}/blank_states_img.gif"
screen.addshape(image)
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()

time_left = 600
guessed_states = []
turtle.shape(image)
turtle.penup()
writes = turtle.Turtle()
writes.hideturtle()
writes.penup()
game_is_on = True

def update_timer():
    global time_left

    # Clear previous time
    timer_turtle.clear()

    global game_is_on
    if time_left >= 0 and game_is_on:
        # Calculate minutes and seconds
        mins, secs = divmod(time_left, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        timer_turtle.goto(200,200)

        # Display the time
        timer_turtle.write(time_format, align="center", font=("Arial", 32, "bold"))

        time_left -= 1

        # Call update_timer again after 1000ms (1 second)
        screen.ontimer(update_timer, 1000)
    else:
        game_is_on = False
        timer_turtle.write("Time's Up!", align="center", font=("Arial", 32, "bold"))
update_timer()
while game_is_on:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt = "what's another state's name?").title()
    data = pd.read_csv(f"{ROOT}/50_states.csv")
    if answer_state is None:
        break
    if answer_state.lower() == "exit":
        game_is_on = False
        missing_states=[]
        for state in data.state.tolist():
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(f"{ROOT}/states_to_learn.csv")
        break
    if answer_state in data.state.values:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

            state_data = data[data.state == answer_state]
            x = int(state_data.x.item())
            y = int(state_data.y.item())
            writes.goto(x, y)
            writes.write(f"{answer_state}")



screen.exitonclick()