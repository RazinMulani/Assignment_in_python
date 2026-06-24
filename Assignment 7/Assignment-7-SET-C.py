# Assignment 7(SET C)
# Q1) Write a Python program to create a dictionary from two lists without losing duplicate values.
# Samplelists:['Class-V','Class-VI','Class-VII','Class-VIII'],[1,2,2,3]
# Expected Output: default dict(<class 'set'>, {'Class-VII': {2},'Class-VI': {2}, 'Class-VIII':{3},
#                'Class-V':{1}})

from collections import defaultdict

classes = ['Class-V','Class-VI','Class-VII','Class-VIII']
numbers = [1,2,2,3]

result = defaultdict(set)


for k, v in zip(classes, numbers):
    result[k].add(v)
print(result)


#Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list
#from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
#Expected Output:
#{'x':[11,12, 13,14,15, 16,17,18, 19],
#'y':[21,22, 23,24, 25,26, 27,28, 29],
#'z':[31, 32,33, 34,35, 36,37, 38, 39]}
#15
#25
#35
# x has value[11, 12,13,14,15, 16,17, 18, 19]
# y has value [21, 22, 23,24, 25, 26, 27, 28,29]
# z has value[31, 32,33, 34,35, 36,37, 38, 39]

my_dict = {
    'x': list(range(11, 20)),
    'y': list(range(21, 30)),
    'z': list(range(31, 40))
}
print(my_dict)
# Access 5th value (index 4)
print(my_dict['x'][4])
print(my_dict['y'][4])
print(my_dict['z'][4])
# Print full values
print("x has value", my_dict['x'])
print("y has value", my_dict['y'])
print("z has value", my_dict['z'])
