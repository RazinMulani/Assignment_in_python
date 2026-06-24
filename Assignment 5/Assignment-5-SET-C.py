# Assignment 5(SET C)
# Q1) Write a Python Program to Interchange First and Last Elements of in a List
'''
lst = [10,20,30,40,50]
lst[0],lst[-1]=lst[-1],lst[0]
print("Interchange First and Last Elements of in a List:",lst)
'''


# Q2) Write a Python Program to Remove Multiple Empty Strings from a List of Strings
l = ["Python","","java","","c","","c++"]
result = []

for i in l:
    if i != "":
        result.append(i)
print("List after removing empty strings:", result)
