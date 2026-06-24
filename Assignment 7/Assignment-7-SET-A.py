# ASSIGNMENT 7(SET A): PYTHON DICTIONARY
# Q1) Write a Python script to access the value of a key from a dictionary.
'''
dic = {
    'a' : 'apple',
    'b' : 'banana',
    'c' : 'cherry'
    }

key = 'b'
print("value of key:", key ,"is:", dic[key])
'''

# Q2)  Write a Python script to concatenate following dictionaries to
# create a new one.
# Sample Dictionary:
# dic1={1:11,2:22}
# dic2={3:33,4:44}
# dic3={5:55,6:66}
# Expected Result: {1: 11,2: 22, 3:33, 4: 44, 5: 55,6:
'''
dic1={1:11,2:22}
dic2={3:33,4:44}
dic3={5:55,6:66}

result={}
result.update(dic1)
result.update(dic2)
result.update(dic3)
print(result)
'''
# Without using method
'''
dic1={1:11,2:22}
dic2={3:33,4:44}
dic3={5:55,6:66}

result={}
for key in dic1:
    result[key] = dic1[key]

for key in dic2:
    result[key] = dic2[key]

for key in dic3:
    result[key] = dic3[key]

print(result)
'''
# Q3) Write a Python program to iterate over dictionaries using for loops.
'''
my_dict = {'a':1, 'b':2, 'c':3}

for key in my_dict:
    print(key ,":",my_dict[key])
'''

# Q4) Write a Python program to sum all the items in a dictionary. Sample Dictionary :
# my_dict={'data1':100,'data2':-54,'data3':247}
# Expected Result: 293
'''
d ={'data1':100,'data2':-54,'data3':247}
total = sum(d.values())
print("Total of dict items:",total)
'''
# Without using sum()
'''
d ={'data1':100,'data2':-54,'data3':247}
total = 0
for i in d:
    total = total + d[i]

print("Total of dict items:",total)
'''

# Q1) Write a Python program to remove a key from a dictionary.
# Sample Dictionary:my Dict={'a':1,'b':2,'c':3,'d':4}
# Sample Output:
# {'c':3,'b':2,'d':4, 'a':1}
# {'c':3,'b':2,'d':4}

d1={'a':1,'b':2,'c':3,'d':4}
print(d1)
# remove using .pop() inbuild method
d1.pop('a')
print("Updated Dictonary:",d1)





