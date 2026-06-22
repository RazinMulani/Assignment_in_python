# Assignment 2(SET-C)
# Q1) Write a program to find the Fibonacci series.
#     First two numbers are 0 and 1
#     Each next number = sum of previous two

'''
n = int(input("Enter The Number:"))

a = 0
b = 1
print("Fibonacci Serirs:")
print(a,b,end=" ")

for i in range(2, n):
    c = a + b
    print(c,end=" ")
    a = b
    b = c
'''
# Q2) Write a Python program to find number is Armstrong or not.
#    (Armstrong number = sum of cubes of digits equals the number)
#     Example: 153 = 1³ + 5³ +

num = int(input("Enter The Number:"))
temp = num
s = 0

while temp > 0:
    digit = temp % 10
    s += digit**3
    temp //= 10

if s == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
