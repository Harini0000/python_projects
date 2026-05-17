from tkinter import *
from tkinter import messagebox
import random
import pandas as pd
from pathlib import Path

# ---------------------------- PATHS ------------------------------- #

ROOT = Path(__file__).resolve().parent

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- LANGUAGE SELECTION WINDOW ------------------------------- #

language_window = Tk()
language_window.title("Choose Language")
language_window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

selected_language = StringVar(value="french")


def confirm_language():
    global LANGUAGE, language_name

    LANGUAGE = selected_language.get()

    if LANGUAGE == "french":
        language_name = "French"
    else:
        language_name = "Dutch"

    language_window.destroy()


title_label = Label(
    language_window,
    text="Choose a Language",
    font=("Arial", 20, "bold"),
    bg=BACKGROUND_COLOR
)

title_label.pack(pady=20)

french_radio = Radiobutton(
    language_window,
    text="French",
    variable=selected_language,
    value="french",
    font=("Arial", 16),
    bg=BACKGROUND_COLOR
)

french_radio.pack(pady=10)

dutch_radio = Radiobutton(
    language_window,
    text="Dutch",
    variable=selected_language,
    value="dutch",
    font=("Arial", 16),
    bg=BACKGROUND_COLOR
)

dutch_radio.pack(pady=10)

confirm_button = Button(
    language_window,
    text="Start Learning",
    font=("Arial", 14, "bold"),
    command=confirm_language
)

confirm_button.pack(pady=20)

language_window.mainloop()

# ---------------------------- LOAD DATA ------------------------------- #

TARGET_LANGUAGE = "English"

try:
    data = pd.read_csv(ROOT / "data" / f"{LANGUAGE}_words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(ROOT / "data" / f"{LANGUAGE}_words.csv")

to_learn = data.to_dict(orient="records")

# ---------------------------- MAIN WINDOW ------------------------------- #

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

current_card = {}

# ---------------------------- FUNCTIONS ------------------------------- #

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas_card.itemconfig(
        card_title,
        text=language_name,
        fill="black"
    )

    canvas_card.itemconfig(
        card_word,
        text=current_card[language_name],
        fill="black"
    )

    canvas_card.itemconfig(
        card_background,
        image=card_front
    )

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas_card.itemconfig(
        card_title,
        text=TARGET_LANGUAGE,
        fill="white"
    )

    canvas_card.itemconfig(
        card_word,
        text=current_card["English"],
        fill="white"
    )

    canvas_card.itemconfig(
        card_background,
        image=card_back
    )


def is_known():
    to_learn.remove(current_card)

    updated_data = pd.DataFrame(to_learn)

    updated_data.to_csv(
        ROOT / "data" / f"{LANGUAGE}_words_to_learn.csv",
        index=False
    )

    next_card()

# ---------------------------- TIMER ------------------------------- #

flip_timer = window.after(3000, func=flip_card)

# ---------------------------- IMAGES ------------------------------- #

cross = PhotoImage(file=ROOT / "images" / "wrong.png")
tick = PhotoImage(file=ROOT / "images" / "right.png")

card_front = PhotoImage(file=ROOT / "images" / "card_front.png")
card_back = PhotoImage(file=ROOT / "images" / "card_back.png")

# ---------------------------- CARD UI ------------------------------- #

canvas_card = Canvas(
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)

card_background = canvas_card.create_image(
    400,
    263,
    image=card_front
)

card_title = canvas_card.create_text(
    400,
    150,
    text="Title",
    font=("Times New Roman", 40, "italic")
)

card_word = canvas_card.create_text(
    400,
    263,
    text="Word",
    font=("Times New Roman", 70, "bold")
)

canvas_card.grid(row=0, column=0, columnspan=2)

# ---------------------------- BUTTONS ------------------------------- #

cross_button = Button(
    image=cross,
    highlightthickness=0,
    command=next_card
)

cross_button.grid(row=1, column=0)

tick_button = Button(
    image=tick,
    highlightthickness=0,
    command=is_known
)

tick_button.grid(row=1, column=1)

# ---------------------------- START ------------------------------- #

next_card()

window.mainloop()