'''
# Assignment-1-SET-C
# Q) 1. Write a Python program to display all keys and values of a dictionary
# Method 1:
student = {"Name":"Razin","Roll_No." : 21,"Marks": 7.14}
for key in student:
    print(key,":",student[key])

# Method 2:


student = {"Name":"Razin","Roll_No." : 21,"Marks": 7.14}
print("keys: ")

for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

'''
# Q) 2. Write a program to create a tuple of five elements and display it
elements = (5,4,6,3,7)
print("Tuple Elemnts Are: ",elements)
