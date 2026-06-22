# Assignment 2(SET-A):
# Operators and Control Structure:
# Q1) Write a Python program to find the sum and percentage of marks obtained in 3 subjects.
'''
sub1 = float(input("Enter The Subject1 Marks: "))
sub2 = float(input("Enter The subject2 Marks: "))
sub3 = float(input("Enter The Subject3 Marks: "))

total = sub1 + sub2 + sub3
percentage = (total/300)*100
print("Total Marks: ",total)
print("Total Percentage: ",percentage)

'''

# Q2) Write a program to check whether a number is even or odd.
'''
num = int(input("Enter The Number: "))

if num %2 == 0:
    print("Number is even")
else:
    print("Number is Odd")
'''
# Q3) Write a program to find sum of a digit of a number.
'''
num = int(input("Enter The Number"))
s = 0

while num > 0:
    d = num % 10
    s += d
    num //= 10

print("Sum of Digit:",s)
'''
# Q4) Write a Python program to check whether a given number is positive, negative, or zero.
'''
num = int(input("Enter The Number"))

if num > 0:
    print("Positive number:")
elif num < 0:
    print("Negative Number:")
else:
    print("zero")
'''
# Q5) Write a program to display numbers from 1 to 10 using a for loop

for i in range(1,11):
    print(i)






















