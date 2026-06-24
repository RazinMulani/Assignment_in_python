# Assignment 6 (SET C)
# Q1) Write a Python program to find the repeated items of a tuple.
'''
t = (1, 2, 3, 4, 2, 5, 3, 6, 1)
repeated_item = []

for i in t:
    if t.count(i) > 1 and i not in repeated_item:
        repeated_item.append(i)

print("repeated item from the tuple:",repeated_item)
'''
# Q2) Write a Python program to check whether an element exists within a tuple

t = (10, 20, 30, 40, 50)
element = 50

if element in t:
    print("Element Exist In Tupple")
else:
    print("Not Exist")
