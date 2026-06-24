# Assignment 8(SET A):- PYTHON SET
# Q1) What is the output of following program: sets = {1, 2, 3, 4, 4} print(sets)
'''
sets = {1, 2, 3, 4, 4}
print(sets)
'''
# Q2) Write a python program to remove and return an arbitrary set element. Raise Key Error if the set
#     is empty

'''
my_set = {10, 20, 30, 40}
if len(my_set) == 0:
    raise KeyError("Set is empty")
else:
    removed = my_set.pop()
    print("Removed element:", removed)
    print("Remaining set:", my_set)
'''

# Q3) Write a Python program to do iteration over sets.
'''
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
'''

# Q4) Write a Python program to add and remove operation on set.
'''
my_set = {1, 2, 3}
# Add element
my_set.add(4)
print("After adding:", my_set)
# Remove element
my_set.remove(2)
print("After removing:", my_set)
'''
