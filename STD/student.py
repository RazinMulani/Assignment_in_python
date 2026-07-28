# Student.py
# import required library

from tkinter import messagebox

# import database function
from database import insert_student

# Import logger
from logger import write_log

# Import Validation Function
from validation import(
    is_empty,
    valid_name,
    valid_age,
    valid_phone,
    valid_email
    )

def add_student(student_data):
    try:
        # insert into MongoDB
        insert_student(student_data)

        if is_empty(student_data["student_id"]):
            messagebox.showerror("Error","Student ID is Required.")
            return

        if is_empty(student_data["name"]):
            messagebox.showerror("Error", "Name is required.")
            return

        if not valid_name(student_data["name"]):
            messagebox.showerror("Error", "Enter a valid name.")
            return

        if not valid_age(student_data["age"]):
    messagebox.showerror("Error", "Enter a valid age.")
    return

if not valid_phone(student_data["phone"]):
    messagebox.showerror("Error", "Enter a valid 10-digit phone number.")
    return

if not valid_email(student_data["email"]):
    messagebox.showerror("Error", "Enter a valid email address.")
    return

        #write Log
        write_log("Student Added Successfully")

        # Success Message
        messagebox.showinfo(
            "Success",
            "Student Added Successfully."
            )
    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
            )

# Validation Code



