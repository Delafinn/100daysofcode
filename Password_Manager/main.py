from tkinter import *
from tkinter import messagebox
import random

BLACK = "#282a36"
RED = "#ff5555"
WHITE = "#f8f8f2"


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
fulllist = letters + numbers + capletters

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global fulllist

    password_entry.delete(0,END)

    passwordlist = [random.choice(fulllist) for _ in range(random.randint(8,9))]
    random.shuffle(passwordlist)

    password = "".join(passwordlist)

    password_entry.insert(0,f"{password}")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    saved_website = website_entry.get()
    saved_emailusername = email_entry.get()
    saved_password = password_entry.get()

    if len(saved_website) == 0 or len(saved_emailusername) == 0 or len(saved_password) == 0:
        messagebox.showinfo(title = "Yikes", message = "Make sure all fields are complete!")

    else:

        is_ok = messagebox.askokcancel(title = "Success!", message = "User data has been saved!")

        if is_ok:

            with open(f"saved_passwords.txt", mode = "a") as file:
                file.write(f" \n {saved_website} , {saved_emailusername} , {saved_password} ")
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
#creating the window of the app
window = Tk()
#setting the title of the app
window.title("PassHole the Password manager")
window.minsize(width = 400, height = 400)
window.config(padx = 20, pady = 20, bg = BLACK)

#making the main label
title_label = Label(text = "PassHole", fg = WHITE, bg = BLACK, font = ("Courier",32,"bold"))
title_label.grid(column = 1 , row = 0)
# creating the canvas for the photo to sit
canvas = Canvas(width = 320, height = 320, bg = BLACK , highlightthickness = 0 )
photo1 = PhotoImage(file = "lock.png")
canvas.create_image(160,160, image = photo1)
canvas.grid(column = 1, row = 2,pady = 20)

website = Label(text = "Website:")
website.grid(column = 0, row = 3)

website_entry = Entry(width = 20)
website_entry.focus()
website_entry.grid(column = 1 , row = 3 , columnspan = 1)

email_username = Label(text = "Email/Username:")
email_username.grid(column = 0 , row = 4)

email_entry = Entry(width = 22)
email_entry.grid(column = 1 , row = 4 , columnspan = 1)

password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 5)

password_entry = Entry(width = 12)
password_entry.grid(column = 1 , row = 5 , columnspan = 1)

add_button = Button(text = "Add",width = 33, command = save_password)
add_button.grid(column = 1, row = 6,columnspan = 2)

generate_password = Button(text = "Generate password",width = 32,command = generate_password)
generate_password.grid(column = 2, row = 5)


exit = Button(text="exit", command=window.destroy)
exit.grid(column = 3, row = 7)



window.mainloop()
