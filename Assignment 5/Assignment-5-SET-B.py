# Assignmnet 5(SET B)
# Q1 Write a Python program to remove duplicates from a list
'''
l = [1,2,3,2,4,1,5]
new_l = []
for i in l:
    if i not in new_l:
        new_l.append(i)
print("After removing duplicates",new_l)
'''

# Q2) Write a Python program to copy a list.
'''
lst = [45,32,90,54]
copy_lst = lst.copy()
print("Orignal List:",lst)
print("Copy List:",copy_lst)

# without using method
lst = [45,32,90,54]

copy_lst = []
for i in lst:
    copy_lst.append(i)
print("OG list:",lst)
print("Copy List:",copy_lst)
'''

# Q3) Write a Python program that removes all even numbers from a specified list and displays the
#  remaining elements.
'''
lst2 = [1,2,3,4,5,6,7,8,9,10]
result = []
for i in lst2:
    if i % 2 != 0:
        result.append(i)
print("After removing Even Number:",result)
'''

# Q4) Write a Python program to append a list to the second list.
'''
lst3 = [1,2,3]
lst4 = [4,5,6]
lst4.extend(lst3)
print("After appending:",lst4)
'''
# without using .extend()
'''
lst5 = [1,2,3]
lst6 = [4,5,6]

for i in lst5:
    lst6.append(i)
print("After appending:",lst6)
'''
# Q5) Write a Python Program to Square Each Element of the List and Print List in Reverse Order
'''
lst7 = [1,2,3,4,5]
lst_square = []
for i in lst7:
    lst_square.append(i*i)

print(lst_square)
lst_square.reverse()
print("Squared and reverse list:",lst_square)
'''

# Q6) Write a Python Program to Remove All Occurrences of an Element from a Given List
lst8 = [1,2,3,2,4,2,5]
element = 2

result = []
for i in lst8:
    if i != element:
        result.append(i)
print("List after removing all occurrences of an Elemnent:",element,":",result)




















