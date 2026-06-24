# Assignment 8 (SET C)
# Q1)  Write a Python program to perform different set operations.
'''
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A - B):", A - B)
print("Difference (B - A):", B - A)
print("Symmetric Difference:", A ^ B)
'''

# Q2) Write a Python program to create shallow copy of sets.

original_set = {1, 2, 3, 4}
# Shallow copy

copied_set = original_set.copy()
print("Original set:", original_set)
print("Copied set:", copied_set)
