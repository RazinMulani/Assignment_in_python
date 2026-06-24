# Assignment 7(SET B)
# Q1) Write a Python program to sort a dictionary by key. Sample Dictionary:
# color_dict={'red':'#FF0000','green':'#008000','black':'#000000','white':'#FFFFFF'}
# Expected Output: black:#000000green:#008000 red: #FF0000 white:#FFFFFF
'''
color_dict={
    'red':'#FF0000',
    'green':'#008000',
    'black':'#000000',
    'white':'#FFFFFF'
    }

for key in sorted(color_dict):
    print(key,":",color_dict[key],end=" ")
'''
## Manual sorting using nested loop
'''
color_dict={
    'red':'#FF0000',
    'green':'#008000',
    'black':'#000000',
    'white':'#FFFFFF'
    }

keys = list(color_dict.keys())

for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        if keys[i] > keys[j]:
            keys[i],keys[j] = keys[j],keys[i]

for key in keys:
    print(key,":",color_dict[key],end = "")
'''

# Q2) . Write a Python program to combine two dictionary adding values for common keys.
# Sample Dictionary:
# d1={'a':100,'b':200,'c':300}
# d2={'a':300,'b':200,'d':400}
# Sample out put: Counter({'a':400, 'b':400,'d':400,'c':300})
'''
from collections import Counter

d1={
    'a':100,
    'b':200,
    'c':300
    }
d2={
    'a':300,
    'b':200,
    'd':400
    }

result = Counter(d1) + Counter(d2)
print(result)
'''
# without using Counter
'''
d1={
    'a':100,
    'b':200,
    'c':300
    }
d2={
    'a':300,
    'b':200,
    'd':400
    }

result = {}
for key in d1:
    result[key] = d1[key]

for key in d2:
    if key in result:
        result[key] += d2[key]
    else:
        result[key] = d2[key]

print(result)
'''
# Q3)  Write a Python script to generate and print a dictionary that
# contains a number (Between 1 and n) in the form (x, x*x).
# Sample Dictionary (n=5)
# Expected Output : {1:1,2: 4, 3: 9, 4:16, 5: 25}
'''
n = 5
my_dict = {}

for x in range(1, n+1):
    my_dict[x] = x * x
print(my_dict)
'''
# Q4) Write a Python program to create a dictionary from a string.
# Sample String:‟W3resource‟
# Expected output:{'3':1,'s':1,'r':2, 'u':1,'w':1, 'c':1,'e':2,'o':1}

string = "W3resource"
my_dict = {}

for ch in string.lower():
    if ch in my_dict:
        my_dict[ch] += 1
    else:
        my_dict[ch] = 1
print(my_dict)












