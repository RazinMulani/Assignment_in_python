# Assignment 6(SET A) : Python TUPLE
# Q1)  Reverse the following tuple Tup=(15,25,35,45,55)
'''
tup = (15,25,35,45,55)
rev = tup[::-1]
print("Actual Tuple:",tup)
print("Reverse Tuple:",rev)
'''
# Q2) Write a Python program to create a list of tuples with the first element as the number and second
#     element as the square of the number.
'''
t = []
for i in range(1,6):
    t.append((i,i*i))
print("List of tuples:",t)
'''

#  Q3) Write a Python program to create a tuple with numbers and print one item.
'''
t1 = (1,2,3,4,5,6)
print("One Item From Tuple:",t1[2])
'''

# Q4) Write a Python program to unpack a tuple in several variables.
'''
t2 = (100,200,300)
a,b,c = t2
print("a = ",a)
print("b = ",b)
print("c = ",c)
'''

# Q4) Write a Python program to add an item in a tuple.
#note:(Tuples are immutable, so we convert to list and back)
'''
tup = (10,20,30,40)
lst = list(tup)
lst.append(50)
tup1 = tuple(lst)
print("Updataed Tuple:",tup1)
'''

# Copy element 22 and 66 from the following tuple in to anewtuple
# tuple1 = (11, 22, 33, 44, 55, 66)

tuple1 = (11, 22, 33, 44, 55, 66)
newtuple = (tuple1[1],tuple1[5])
print("New Tuple:",newtuple)











