from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Georgia"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(time, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # For the 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        window.wm_attributes("-topmost", True)
        window.wm_attributes("-topmost", False)

    # For the 2nd, 4th, and 6th rep (all even)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        window.wm_attributes("-topmost", True)
        window.wm_attributes("-topmost", False)

    # For the 1st, 3rd, 5th, and 7th rep (all odd)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for session in range(work_session):
            marks += " 🗹 "
        check_marks.config(text=marks)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=288, height=282, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(144, 141, image=tomato_image)
time = canvas.create_text(144, 159, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=2, row=2)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
title_label.grid(column=2, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 15), command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 15), command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_marks.grid(column=2, row=4)

window.mainloop()
