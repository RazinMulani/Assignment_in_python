# Assignment 5(SET A) : Python LIST
# Q1)  Write a Python program to sum all the items in a list.
'''
l = [10,20,30,40,50]
total = 0
for i in l:
    total = total + i
print("Total:",total)
'''

# Q2) Write a Python program to multiplies all the items in a list.
'''
lst = [10,20,30,40,50]
product = 1
for i in lst:
    product = product * i
print("Product:",product)
'''

# Q3) Write a Python program to get the largest number from a list.
'''
lst1 = [45,12,78,42,90]
largest = lst1[0]
for i in lst1:
    if i > largest:
        largest = i
print("Largest No:",largest)
'''
# Q4) Write a Python program to get the smallest number from a list.
'''
lst2 = [45,78,42,12,90]
smallest = lst2[0]
for i in lst2:
    if i < smallest:
        smallest = i
print("Smallest No.:",smallest)
'''

# Q5)  Write a Python program to check if a list is empty or not
lst3 = []
if len(lst3) == 0:
    print("List is Empty")
else:
    print("List is Full")












