from tkinter import *
import random
import pandas as pd
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent


BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv(f"{ROOT}/data/french_words_to_learn.csv")
except FileNotFoundError:
    data= pd.read_csv(f"{ROOT}/data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn= data.to_dict(orient="records")


current_card = {}


def next_card() :
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas_card.itemconfig(card_title, text="French", fill="black")
    canvas_card.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas_card.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000,func=flip_card)


def flip_card() :
    canvas_card.itemconfig(card_title, text="English", fill="white")
    canvas_card.itemconfig(card_word, text= current_card["English"], fill="white")
    canvas_card.itemconfig(card_background, image=card_back)

def is_known() :
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(f"{ROOT}/data/french_words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashcard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

cross=PhotoImage(file=f"{ROOT}/images/wrong.png")
tick=PhotoImage(file=f"{ROOT}/images/right.png")
card_front=PhotoImage(file=f"{ROOT}/images/card_front.png")
card_back=PhotoImage(file=f"{ROOT}/images/card_back.png")

canvas_card = Canvas(width=800, height =526)
card_background = canvas_card.create_image(400,263, image=card_front)
canvas_card.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas_card.create_text(400,150,text="Title",font=("Times New Roman",40,"italic"))
card_word=canvas_card.create_text(400,263,text="word",font=("Times New Roman",70,"bold"))
canvas_card.grid(row=0,column=0,columnspan=2)

cross_button=Button(image=cross,highlightthickness=0, command=next_card)
cross_button.grid(row=1,column=0)
tick_button=Button(image=tick,highlightthickness=0, command=is_known)
tick_button.grid(row=1,column=1)

next_card()

window.mainloop()