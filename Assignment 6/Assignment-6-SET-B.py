# Assignment 6 (SET B)
# Q1)  Write a Python program to convert a tuple to a string.
tup = ('p','y','t','h','o','n')
string = ''.join(tup)
print("String:",string)

# Q2) Sort the tuple: Tuple=(2, 4,6, 1, 4, 7.8, 2.7)
tup1 = (2, 4,6, 1, 4, 7.8, 2.7)
sorted_tup = tuple(sorted(tup1))
print("Sorted Tuple:",sorted_tup)

# Q3) Write a Python program to get the 4th element from front and 6th element from last of a tuple.
tup2 = (10, 20, 30, 40, 50, 60, 70, 80)

print("4th elemnt from tuple:",tup2[4])
print("6th element from the last of the tuple:",tup2[-6])
