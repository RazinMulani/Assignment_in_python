# ASSIGNMENT 4(SET A)
# Python Function
# Q1) Write a Python function to find the Max of three numbers.
'''
# using max method
def fun1(a,b,c):
    return max(a,b,c)
print(fun1(20,40,23))

def fun1():
    a = 30
    b = 45
    c = 23
    return max(a,b,c)
print(fun1())
'''
'''
# using without method
def max_num(a,b,c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)
max_num(10,20,5)
'''
'''
# Q2)Write a Python program to reverse a string.

def reverse_str(s):
    print(s[::-1])

s = input("Enter A String:")
reverse_str(s)
'''
'''
def r_str(s):
    rev = ""
    for i in s:
        rev = i + rev
    print(rev)

s = input("Enter The String:")
r_str(s)
'''

# Q3)Write an anonymous function to calculate area of square.
'''
areaof_square = lambda side : side * side
print("area of square",areaof_square(5))

# get input from user
areaof_square = lambda s: s * s
s = input("Enter The value:")

if s.isdigit():
    s = int(s)
    print("Area of Square:",areaof_square(s))
else:
    print("Pls Enter valid Number")
'''

# Q4) Write a Python function to check whether a number is in a given range.
'''
def is_in_range(num,start,end):
    if start <= num <= end:
        print(True)
    else:
        print(False)
is_in_range(7,1,10) # is in range(True)
 
def is_in_range(num,start,end):
    if start <= num <= end:
        print(True)
    else:
        print(False)
is_in_range(3,4,10) # is not in range(False)

#using return keyword
def is_in_range(num,start,end):
    return start <= num <= end

print(is_in_range(6,1,10))
'''

# Q5) Write a Python function that accepts a string and calculate the number of uppercase lettersand lower case letters.
'''
def count_letter(s):
   
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("lower letter:",lower)
    print("upper letter:",upper)
    print("Total letter in string:",lower+upper)
s = input("Enter The string:")
count_letter(s)
'''
# Q6) Write a python functions to calculate the area of different geometric shapes (e.g., circle,
#    rectangle,triangle) based on provided dimensions.

'''
def area_of_geometric_shap():
    def circule():
        print("Find The Area Of Circule-------------")
        pi = 3.14
        r = int(input("Enter the radius:"))
        print("Area of Circule is:", pi*r*r)
    circule()

    def rectangle():
        print("Find The Area Of reactangle-------------")
        l = int(input("Enter the length:"))
        b = int(input("Enter the Breadth:"))
        print("Area of reactangle:",l*b)
    rectangle()

    def triangle():
        print("Find The Area Of Triangle-------------")
        b = int(input("Enter the base:"))
        h = int(input("Enter the height:"))
        print("Area  of traingle:",0.5*b*h)
    triangle()
area_of_geometric_shap()

'''
# using import math and return keyword
'''
import math

def area_circle(radius):
    return math.pi * radius * radius
def area_rectangle(length, width):
    return length * width
def area_triangle(base, height):
    return 0.5 * base * height
print("Area of Circle:", area_circle(5))
print("Area of Rectangle:", area_rectangle(4, 6))
print("Area of Triangle:", area_triangle(3, 8))

'''
# Q7)  Write python program that inputs a number and prints the multiplication table of that numberusing function
def table(n):
    for i in range(1,11):
        print(n , " x ",i," = ",n*i)

table(2)




