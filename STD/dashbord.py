# dashbord.py

# import tkinter library
from tkinter import *
from tkinter import ttk
from student import add_student
from tkinter import filedialog

def upload_photo():
    filename = filedialog.askopenfilename(
        title="Select Student Photo",

        filetypes=[
            ("Images Files", "*.png *.jpg *.jpeg")
            ]
        )
    if filename:
        photo_path.set(filename)
        print(filename)
        

# main window

root = Tk()

root.title("Student Managment System")
root.geometry("1350x700")
root.resizable(False,False)
root.configure(bg="white")

# Heading

title = Label(
    root,
    text="Student Managment System",
    fg= "white",
    bg="#0B5394",
    font=("Arial",20,"bold"),
    pady=10
    )
title.pack(fill=X)## Fill Complete Width

#left frame
student_frame = LabelFrame(
    root,
    text="Student Details",
    font=("Arial",12,"bold"),
    bg="white",
    padx = 10,
    pady =10
    )
student_frame.place(
    x = 20,
    y = 70,
    width = 420,
    height = 600
    )



# Student Details
# Student ID
Label(
    student_frame,
    text="Student ID",
    font=("Arial",11),
    bg="white"
    ).grid(row=0,column=0,padx=10,pady=10,sticky=W)

student_id = StringVar()
student_id_entry = Entry(
    student_frame,
    textvariabl =student_id,
    font=("Arial",11),
    width=25
    )

student_id_entry.grid(row=0, column=1, padx=10, pady=10)

#Student Name
Label(
    student_frame,
    text="Student Name",
    font=("Arial",11),
    bg="white"
    ).grid(row=1,column=0,padx=10,pady=10,sticky=W)

name = StringVar()
name_entry = Entry(
    student_frame,
    textvariabl =name,
    font=("Arial",11),
    width=25
    )

name_entry.grid(row=1, column=1, padx=10, pady=10)
# Student Age

Label(
    student_frame,
    text="Student Age",
    font=("Arial",11),
    bg="white"
    ).grid(row=2,column=0,padx=10,pady=10,sticky=W)

age = StringVar()
age_entry = Entry(
    student_frame,
    textvariabl =age,
    font=("Arial",11),
    width=25
    )

age_entry.grid(row=2, column=1, padx=10, pady=10)
# Students Gender 
Label(
    student_frame,
    text="Student Gender",
    font=("Arial",11),
    bg="white"
    ).grid(row=3,column=0,padx=10,pady=10,sticky=W)

gender = StringVar()
Radiobutton(
    student_frame,
    text="Male",
    variable=gender,
    font=("Arial",11),
    value="Male",
    bg="white"
    ).grid(row=3, column=1,sticky=W)

Radiobutton(
    student_frame,
    text="Female",
    variable=gender,
    font=("Arial",11),
    value="Female",
    bg="white"
    ).grid(row=3,column=1,padx=80,sticky=W)

# Course (Combobox)
Label(
    student_frame,
    text="Course",
    font=("Arial",11),
    bg="white"
    ).grid(row=4,column=0,padx=10, pady=10,sticky=W)

course =StringVar()

course_box = ttk.Combobox(
    student_frame,
    textvariable=course,
    width=23,
    state="readonly"
    )
course_box["values"]=(
    "Computer Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electrical Engineering",
    "Electronics Engineering",
    "Information Technology"
    )
course_box.grid(row=4,column=1,padx=10,pady=10)
course_box.current(0)

# Phone
Label(
    student_frame,
    text="Student Phone Number",
    font=("Arial",11),
    bg="white"
    ).grid(row=5,column=0,padx=10,pady=10,sticky=W)

phone = StringVar()
phone_entry = Entry(
    student_frame,
    textvariabl =phone,
    font=("Arial",11),
    width=25
    )

phone_entry.grid(row=5, column=1, padx=10, pady=10)

# Email
Label(
    student_frame,
    text="Student Email",
    font=("Arial",11),
    bg="white"
    ).grid(row=6,column=0,padx=10,pady=10,sticky=W)

email = StringVar()
email_entry = Entry(
    student_frame,
    textvariabl =email,
    font=("Arial",11),
    width=25
    )

email_entry.grid(row=6, column=1, padx=10, pady=10)

# Address
Label(
    student_frame,
    text="Student Address",
    font=("Arial",11),
    bg="white"
    ).grid(row=7,column=0,padx=10,pady=10,sticky=NW)

address = Text(
    student_frame,
    width=25,
    height=4,
    font=("Arial",11)
    )
address.grid(row=7, column=1, padx=10, pady=10)

#upload Photo
Label(
    student_frame,
    text="Photo",
    font=("Arial",11),
    bg="white"
    ).grid(row=8,column=0, padx=10, pady=10, sticky=W)

photo_path = StringVar()

photo_entry =Entry(
    student_frame,
    textvariable = photo_path,
    width=15,
    state="readonly",
    font=("Arial",11)
    )
photo_entry.grid(row=8, column=1, padx=10, pady=10)
# Upload Button
upload_btn = Button(
    student_frame,
    text="Browse",
    bg="red",
    width =8,
    command=upload_photo
    )

upload_btn.grid(row=9, column=1, padx=5,pady=10)

# Right Farame
record_frame = LabelFrame(
    root,
    text="Student Records",
    font=("Arial",12,"bold"),
    bg="white",
    padx=10,
    pady=10
    )
record_frame.place(
    x=460,
    y=70,
    width=870,
    height=600
    )
# Search Frame

search_frame = Frame(
    record_frame,
    bg="white"
    )
search_frame.pack(fill=X, pady=5)
# Search Label
Label(
    search_frame,
    text="Search By",
    font=("Arial",11,"bold"),
    bg="white"
    ).grid(row=0, column=0, padx=5, pady=5)
# Search Combobox
search_by = StringVar()

search_combo = ttk.Combobox(
    search_frame,
    textvariable = search_by,
    width=18,
    state="readonly"
    )

search_combo["values"]=(
    "Student Id",
    "Name",
    "Phone",
    "Course"
    )

search_combo.current(0)
search_combo.grid(row=0,column=1, padx=5)

#Search Entry
search_text =StringVar()

search_entry = Entry(
    search_frame,
    textvariable=search_text,
    width=25,
    font=("Arial",11)
    )

search_entry.grid(row=0, column=2, padx=5)

# Search button
search_btn =  Button(
    search_frame,
    text="Search",
    width=10
    )
search_btn.grid(row=0,column=3,padx=5)

# Search Show All Button
show_all_btn = Button(
    search_frame,
    text="Show All",
    width=10
)

show_all_btn.grid(row=0, column=4, padx=5)

# 

# Treeview
# Vertical Scroll Bar
scroll_y = Scrollbar(record_frame, orient=VERTICAL)
#Horizontal Scroll Bar
scroll_x = Scrollbar(record_frame, orient=HORIZONTAL)

# Create Treeview
student_table = ttk.Treeview(
    record_frame,

    columns=(
        "student_id",
        "name",
        "age",
        "gender",
        "course",
        "phone",
        "email",
        "address"
        ),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
    )

# Connect Scroll Bar
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

# Create Heading
student_table.heading("student_id", text="Student ID")

student_table.heading("name", text="Name")

student_table.heading("age", text="Age")

student_table.heading("gender", text="Gender")

student_table.heading("course", text="Course")

student_table.heading("phone", text="Phone")

student_table.heading("email", text="Email")

student_table.heading("address", text="Address")

# Set Colum Width

student_table.column("student_id", width=120)

student_table.column("name", width=150)

student_table.column("age", width=70)

student_table.column("gender", width=100)

student_table.column("course", width=180)

student_table.column("phone", width=120)

student_table.column("email", width=220)

student_table.column("address", width=250)

# Show Only Heading
student_table["show"]="headings"

# Desplay Treeview
student_table.pack(fill=BOTH, expand=True)


# Button Frame
button_frame = LabelFrame(
    root,
    text="Operations",
    font=("Arial", 12, "bold"),
    bg="white"
    )

button_frame.place(
    x=440,
    y=610,
    width=900,
    height=70
    )



# Save Student Data
def save_student():
    student = {
        "student_id": student_id.get(),
        "name":name_entry.get(),
        "age":age_entry.get(),
        "gender":gender.get(),
        "course":course_box.get(),
        "phone":phone_entry.get(),
        "email":email_entry.get(),
        "address":address.get("1.0",END).strip()
        }
    add_student(student)
# Create Operations Button
# Add Button
add_btn = Button(
    button_frame,
    text="Add",
    width=12,
    font=("Arial",10,"bold"),
    bg="#4CAF50",
    fg="white",
    command=save_student)

add_btn.grid(row=0,column=0,padx=5,pady=10)

# update Button
update_btn = Button(
    button_frame,
    text="Update",
    width=12,
    font=("Arial",10,"bold"),
    bg="#2196F3",
    fg="white")

update_btn.grid(row=0,column=1,padx=5,pady=10)

# Delete Button
delete_btn = Button(
    button_frame,
    text="Delete",
    width=12,
    font=("Arial",10,"bold"),
    bg="#F44336",
    fg="white")

delete_btn.grid(row=0,column=2,padx=5,pady=10)

# Clear Field
def clear_fields():
    student_id.set("")
    name.set("")
    age.set("")
    gender.set("Male")
    course_box.current(0)
    phone.set("")
    email.set("")
    address.delete("1.0",END)
    
# Clear Button
clear_btn = Button(
    button_frame,
    text="Clear",
    width=12,
    font=("Arial",10,"bold"),
    bg="#FF9800",
    fg="white",
    command=clear_fields)

clear_btn.grid(row=0,column=3,padx=5,pady=10)

# Search Button
search_btn = Button(
    button_frame,
    text="Search",
    width=12,
    font=("Arial",10,"bold"),
    bg="#9C27B0",
    fg="white")

search_btn.grid(row=0,column=4,padx=5,pady=10)
# Show All Button
show_btn = Button(
    button_frame,
    text="Show All",
    width=12,
    font=("Arial",10,"bold"),
    bg="#009688",
    fg="white")

show_btn.grid(row=0,column=5,padx=5,pady=10)
# Exit Button
exit_btn = Button(
    button_frame,
    text="Exit",
    width=12,
    font=("Arial",10,"bold"),
    bg="black",
    fg="white",
    command=root.destroy
    )

exit_btn.grid(row=0,column=6,padx=5,pady=10)
root.mainloop()




