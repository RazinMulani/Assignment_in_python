'''
# Assignment-1-SET-B
# Q) 1.Write a Python program to show proper indentation using an if statement.

num = 10

if num > 5:
    print("Nummber is grater than 5:")
    print("This statment is inside the if block")

print("This statment is outside the if block")
'''
'''
# Q) 2.Write a program to display the type of each variable using the type() function.

a = 10
b = 23.3
c = 3 + 1j
d = "Python"

print("Value of a",a,"Type of",type(a))
print("Value of b",b,"Type of",type(b))
print("Value of c",c,"Type of",type(c))
print("Value of d",d,"Type of",type(d))
'''
'''
# Q) 3.Write a program to take multiple inputs from the user in a single line
a,b,c = input("Get the value from the user and seprated by the space").split()
print("Enter The value of a:",a)
print("Enter The value of b:",b)
print("Enter The value of c:",c)
'''
'''
# Q) 4. Write a Python program to accept user input for a list of numbers and display the list.
# method 1

numbers = input("Enter number seprated by the space").split()
numbers = list(map(int, numbers))
print(numbers)

# method 2

numbers=[]
n = int(input("how many numbers?"))
for i in range(n):
    num = int(input("Enter The Numbers"))
    numbers.append(num)

print("The list of number is:",numbers)
'''
'''
# Q) 5. Write a Python program that takes student details (name, roll number, marks) as input and displays them in a formatted manner
# Method 1:

name = input("Enter the name of the Student: ")
roll_num = int(input("Enter The Roll  No. Of The Student: "))
marks = float(input("Enter The Marks Of The Students: "))

print("\n--Students Details --")
print("Std Name    : ",name)
print("Std Roll No.: ",roll_num)
print("Std Marks   : ",marks)
'''

# method 2:
name = input("Enter the name of the Student: ")
roll_num = int(input("Enter The Roll  No. Of The Student: "))
marks = float(input("Enter The Marks Of The Students: "))

print(f"Std Name: {name}, Std Roll_num{roll_num}, Std Marks{marks}")
