''' Convert Miles to Kilometers '''
from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=300, height=200)

Mile_Entry = Entry(width = 10)
Mile_Entry.grid(column = 3, row = 2)

label1 = Label(text = "Miles", font = ("Arial" , 18 ,"bold" ))
label1.grid(column = 4, row = 2)

label2 = Label(text = "is equal to:", font = ("Arial" , 18 ,"bold" ))
label2.grid(column = 2, row = 3)

def button_click():
    ''' with the button click multiply the mile entry by 1.609'''
    new_text = float(Mile_Entry.get())
    new_text *= 1.609
    label3.config(text = new_text)

button = Button(text = "Calculate", command = button_click)
button.grid(column = 3, row = 4)

label3 = Label(text = "", font = ("Arial" , 18 ,"bold" ))
label3.grid(column = 3, row = 3)

label4 = Label(text = "Kilometers", font = ("Arial" , 18 ,"bold" ))
label4.grid(column = 4, row = 3)






window.mainloop()
