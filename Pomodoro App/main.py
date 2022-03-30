from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
GREY = "#EAEAEA"
RED = "#FF2E63"
TEAL = "#08D9D6"
BLACK = "#252A34"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    '''resetting the widgets of the Pomodoro app '''
    #stops the timertext on line 67
    window.after_cancel(TIMER)
    # reset timer
    canvas.itemconfig(timertext, text = "00:00")
    # title_label should be timer
    title_label.config(text = "TIMER")
    # reset checkmarks
    checkmarks.config(text = "")
    # reset REPS
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_seconds = WORK_MIN * 60
    short_seconds = SHORT_BREAK_MIN * 60
    long_seconds = LONG_BREAK_MIN * 60


    #elif its the 8th rep we want to use LONG_BREAK_MIN
    if REPS % 8 == 0:
        title_label.config(text = "Break Time",fg = GREY)
        count_down(long_seconds)

    #else we want to use SHORT_BREAK_MIN
    elif REPS % 2 == 0:
        title_label.config(text = "Break Time",fg = RED)
        count_down(short_seconds)
    else:
        title_label.config(text= "Work Time")
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timertext, text= f"{count_min}:{count_sec}")

    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for scndrep in range(work_sessions):
            marks += "✓"
        checkmarks.config(text = marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro app")
window.minsize(width=400, height=400)
window.config(padx = 100, pady = 50, bg = BLACK)



title_label = Label(text = "TIMER", fg = TEAL, bg = BLACK, font=(FONT_NAME, 42, "bold"))
title_label.grid(column = 2, row = 0)


canvas = Canvas(width = 200, height = 224, bg = BLACK , highlightthickness = 0 )
photo1 = PhotoImage(file = "tomato.png")
canvas.create_image(100,112 , image = photo1)
timertext = canvas.create_text(100,140, text = "00:00", fill = "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 2, row = 2)




#calls start_action() when pressed
start = Button(text="start", command=start_timer)
start.grid(column = 1, row = 3)

#calls reset_timer() when pressed
reset = Button(text="reset", command=reset_timer)
reset.grid(column = 3, row = 3)

#calls window.destroy action() when pressed
exit = Button(text="exit", command=window.destroy)
exit.grid(column = 2, row = 5)

#appears when a full cycle has been completed
checkmarks = Label(text = "",fg = TEAL, bg = BLACK, font=(FONT_NAME, 42, "bold"))
checkmarks.grid(column = 2, row = 4)






window.mainloop()
