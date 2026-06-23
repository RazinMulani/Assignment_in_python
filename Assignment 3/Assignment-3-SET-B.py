# Assignment 3(SET B)
# Q1.) Write a python program to print even length words in a string
# Accept a string
# Split string into words
# Check length of each word
# Print word if length is even
'''
s = input("Enter The String:")
words = s.split()

print("Even Length words of:")
for word in words:
    if len(word) % 2 == 0:
        print(word)
# input: Razin Rafik Mulani
# outpu: Mulani(Even Length)
'''

# Q2)  Write a python program to accept the strings which contains all vowels Check whether a string
#      contains all five vowels
#  (a, e, i, o, u)
#  Convert string to lowercase
#  Check presence of each vowel
#  If all present → valid string
'''
s1 = input("Enter The String:").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}

if vowels.issubset(set(s1)):# issubset(): "Check if all elements of one set exist inside another set."
    print("String contains all vowel")
else:
    print("String does NOT contain all vowels")

'''

# Q3) Count how many common characters appear in both strings
# (No duplicates counted twice)
# Convert both strings into sets
# Find intersection
# Count matching characters
'''
string1 = input("Enter First String")
string2 = input("Enter Second String")

matching = set(string1)&set(string2) # '&' means intersection.
print("Matching Characters:",matching)
print("Number of matching Characters:",len(matching))
'''
# Q4) Write a python program to arrange string characters such that lowercase letters should come first
# Separate lowercase characters
# Separate uppercase characters
# Combine them
'''
S = input("Enter The String")

lower = " "
upper = " "

for i in S:
    if i.islower():
        lower += i
    else:
        upper += i
result = lower + upper
print("Rearranged String:",result)
'''

# Q5) Write a python program to replace special symbol in string with '#'character.

# Traverse string
# If character is not alphanumeric → replace with #
'''
s3 = input("Enter The String:")
result = ""

for i in s3:
    if i.isalnum():
        result += i
    else:
        result += '#'

print("modified string:", result)

'''

# Q6) Write a python program to convert half of the string to uppercase
# Input : python Output : PYThon or python
# Find middle index
# Convert either:First half to uppercase ORSecond half to uppercase

s4 = input("Enter The String")
mid = len(s4)// 2

result = s4[:mid].upper()+s4[mid:]
print("Result:",result)






