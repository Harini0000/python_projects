import tkinter as tk
import time
import math
from tkinter.tix import IMAGE

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    check_mark.config(text="")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps %2 !=0:
        count_down(work_sec)
        title_label.config(text="Work time", fg=GREEN, bg=YELLOW)
    elif reps %8  == 0:
        count_down(long_break_sec)
        title_label.config(text=" break time", fg=RED, bg=YELLOW)
    else:
        count_down(short_break_sec)
        title_label.config(text=" break time", fg=PINK, bg=YELLOW)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec == 1 or count_sec ==2 or count_sec ==3 or count_sec ==4 or count_sec ==5 or count_sec ==6 or count_sec ==7 or count_sec ==8 or count_sec ==9:
        count_sec = str(count_sec)
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔ \n"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("POMODORO")
window.config(padx=50, pady=50, bg=YELLOW)


title_label = tk.Label(text="Timer", fg = GREEN,bg=YELLOW,font=(FONT_NAME,50,'bold'))
title_label.grid(row=0,column=1)

canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_img )
timer_text=canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)

start_button=tk.Button(text="start", command=start_timer)
start_button.grid(row=2,column=0)

reset_button=tk.Button(text="reset", command= reset_timer)
reset_button.grid(row=2,column=2)

check_mark=tk.Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(row=3,column=1)



window.mainloop()
