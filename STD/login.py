# login.py

# required Libraries

from tkinter import *
from tkinter import messagebox

from config import *

from logger import write_log

# function

def login():
    # Check Entry Username
    #Get Username From Entry Widget
    username = username_entry.get()

    #Get password from Entry Widget
    password = password_entry.get()

    
    if username == "":
        messagebox.showerror('Error','Please Enter Username')
        return

    if password == "":
        messagebox.showerror('Error','Please Enter Password')
        return

    #temprory login
    #later this will come from MongoDB

    if username == "admin" and password == "1234":
        write_log("Login Successful")

        messagebox.showinfo(
            "Success",
            "Login Successful"
            )
    else:
        write_log("Login Failed")

        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
            )
        
# clear data
def clear_data():
    username_entry.delete(0,END)
    password_entry.delete(0,END)

# Show Password
def show_password():
    #if checkbutton is checked
    if check_value.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")
# Exit Program
def exit_program():
    answer = messagebox.askyesno(
        "Exit",
        "Do You Want To Exit?"
        )
    if answer:
        root.destroy()

# MAIN WINDOW
root = Tk()
root.title(TITLE)
root.geometry("450x420")
root.resizable(False, False)
root.configure(bg="white")

# title
title = Label(root,
              text="Student Management System",
              font=("Arial", 18, "bold"),
              bg="white"
              )
title.pack(pady=20)

# Usernamae

Label(
    root,
    text="Username",
    bg="white",
    font=("Arial", 12)
).pack()

username_entry = Entry(
    root,
    font=("Arial", 12),
    width=30
)
username_entry.pack(pady=5)

# password

Label(
    root,
    text="Password",
    bg="white",
    font=("Arial", 12)
).pack()

password_entry = Entry(
    root,
    show="*",
    font=("Arial", 12),
    width=30
)

password_entry.pack(pady=5)

# Show Password
check_value = IntVar()

Checkbutton(
    root,
    text="Show Password",
    variable=check_value,
    command=show_password,
    bg="white"
    ).pack()

# Login Button
Button(
    root,
    text="Login",
    width=20,
    command=login
).pack(pady=10)

# Cleat Button
Button(
    root,
    text="Clear",
    width=20,
    command=clear_data
).pack()

# Exit Button
Button(
    root,
    text="Exit",
    width=20,
    command=exit_program
).pack(pady=10)


# Start GUI
root.mainloop()
