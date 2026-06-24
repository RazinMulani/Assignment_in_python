# Assignment 4(SET C)
# Q1) 1. Create an inner function to calculate the addition in the following way
#  a. Create an outer function that will accept two parameters a and b
#  b. Create an inner function inside an outer function that will calculate the addition of a and b.
#  c. At last, an outer function will add 5 into addition and return it.
'''
def outer_function(a, b):
    # Inner function
    def inner_function():
        return a + b
    # Call inner function and add 5 to its result
    result = inner_function() + 5
    return result
# Example
print(outer_function(10, 20)) # (10 + 20) + 5 = 35
'''
# Q2) Write a Python program using separate functions to perform the following operations: Addition ,
#Subtraction, Multiplication, Division, Modulus Use a menu-driven approach and call appropriate functions
#based on user choice.
# Separate functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Modulus by zero is not allowed"
    return a % b

# Menu-driven program
while True:
    print("\n----- MENU -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    
    choice = int(input("Enter your choice (1-6): "))

    if choice == 6:
        print("Exiting program...")
        break
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", add(a, b))
    elif choice == 2:
        print("Result =", subtract(a, b))
    elif choice == 3:
        print("Result =", multiply(a, b))
    elif choice == 4:
        print("Result =", divide(a, b))
    elif choice == 5:
        print("Result =", modulus(a, b))
    else:
        print("Invalid choice! Please select from 1 to 6.")






