# Assignment 4 (SET B)
# Q1) Write a python program that converts a decimal number to binary number usingfunction.

'''
def decima_to_binary(n):
    return bin(n)[2:]
num = int(input("Enter the decimal number"))
print(decima_to_binary(num))
'''
# Without using bin()
'''
def decima_to_binary(n):
    binary= ""

    while n > 0:
        reminder = n % 2
        binary = str(reminder)+ binary
        n = n // 2

    print("Binary Number",binary)
num = int(input("Enter Decimal number:"))
decima_to_binary(num)
'''
# What is recursion

# Q2)Write a python program to find the sum of natural number using recursive function.
'''
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)
num = int(input("Enter a number: "))
print("Sum of first", num, "natural numbers:", sum_natural(num))
'''
# Q3) Write a python program to print the Fibonacci sequence using recursive function
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
terms = int(input("Enter number of terms: "))
print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")
'''

# Q4) Write a Python function to check whether a number is perfect or not.
'''
def is_perfect(n):
    if n <= 1:
        return False
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    return sum_div == n
num = int(input("Enter a number: "))
if is_perfect(num):
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
'''
# Q5) Write a Python function that takes a number as a parameter and check the numberis prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")






