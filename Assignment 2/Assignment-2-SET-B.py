# Assignment 2(SET-B)
# Q1) Write a Python program to find the largest of three numbers using nested if-else statements.
'''
num1 = int(input("Enter The Number 1: "))
num2 = int(input("Enter The Number 2: "))
num3 = int(input("Enter The Number 3: "))

if num1 > num2:
    if num1 > num3:
        print("Largest number is Number 1:",num1)
    else:
        print("Largest Number is Number 3:",num3)
else:
    if num2 > num3:
        print("Largest Number is Number 2:",num2)
    else:
        print("Largest Number is Number 3:",num3)
'''

# Q2)  Write a Python program to check that two strings are equal or not. Print appropriate message.
'''
msg1 = input("Enter The First Massage:")
msg2 = input("Enter The Secand Massage:")

if msg1 == msg2:
    print("Bothe Massages are Equal")
else:
    print("Massages are not Equal")
'''
# Q3) Write a Python program to check whether a character is present in a given string or not.
'''
string = input("Enter The String:")
ch = input("Enter a Character to Search:")

if len(ch)!= 1:
    print("Please Enter ONLY ONE CHARACTER:")

else:
    if ch in string:
        print("Character is present in the string")
    else:
        print("Character is not present in the string")
'''

# Q4) Write a Python program to print all even numbers between 1 and 50 using a while loop.
'''
num = 1
while num <= 50:
    if num %2 == 0:
        print("Even Numbers:", num)
    num  += 1
'''
# Q5)  Write a Python program to check number is Perfect or not
#     (Perfect number = sum of its proper divisors equals the number)
'''
num = int(input("Enter The Number"))
s = 0

for i in range(1,num):
    if num % i == 0:
        s += i

if s == num:
    print("Perfect Number")
else:
    ("Not a Perfect Number")

'''
# Q6) Write a Python program to find factorial of a number.

num = int(input("Enter The Number"))
fact = 1

for i in range(1,num+1):
    fact *= i

print("Factorial is:",fact)


















