# Assignment 8 (SET B)
# Q1) Write a Python program to accept the strings which contains all vowels.
'''
string = input("Enter a string: ").lower()
vowels = set('aeiou')
if vowels.issubset(set(string)):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
'''
# Q2)  Write a Python program to create a union of sets.
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)
'''

# Q3) Write a Python program to create an intersection of sets.
'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)
'''

# Q4) Write a Python program to find maximum and the minimum value in a set.
'''
my_set = {10, 5, 30, 25, 15}
print("Maximum:", max(my_set))
print("Minimum:", min(my_set))
'''
# Q5) Write a Python program to create set difference and asymmetric difference
'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Difference
diff = set1 - set2
print("Difference (set1 - set2):", diff)
# Symmetric difference
sym_diff = set1 ^ set2
print("Symmetric Difference:", sym_diff)
'''
# Q6) Write a Python program to find the length of a set.
my_set = {1, 2, 3, 4, 5}
print("Length of set:", len(my_set))






