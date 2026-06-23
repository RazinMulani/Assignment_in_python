# Assignment 3(SET A)
# Python String
# Q1)Write a program to replace all occurrences of “a‟ with $ in a String.
#    (Ex. apple then output is $pple).
'''
# Using .replace() method
s = input("Enter The Massage:")
print("Orignal String: ",s)
result = s.replace('a','$')
print("Replacing Massage: ",result)

# Without using .replace() method

msg = input("Enter The Massage:")
new_msg = " "

for ch in msg:
    if ch == 'a':
        new_msg += '$'
    else:
        new_msg += ch

print("Output:",new_msg)
'''

# Q2) Write a python program to Reverse words in a given String
'''
s = input("Enter Sentence:")
words = s.split()

reversed_words = []
for word in words:
    reversed_words.append(word[::-1])

result = " ".join(reversed_words)
print("Output:",result)
'''
# Q3) Write a Python program to count the number of characters
#     (character frequency) in a string. Sample String: ‘google.com'
#     Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''
s = input("Enter The String:")
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Output:", freq)
'''
# Q4)  Write a python program to check whether the string is Palindrome
'''
s = input("Enter The Sentence")
if s==s[::-1]:
    print("It is palindrom")
else:
    print("It is not a palindrom")

'''

# Q5) Write a Python program to calculate the Length of a String without using a Library Function.

'''
s = input("Enter string:")
count = 0

for ch in s:
    count += 1

print("Length of a string:",count)
'''

# Q6) Calculate the sum and average of the digits present in a string

s = input("Enter The String:")
total = 0
count = 0

for ch in s:
    if ch.isdigit():
        total += int(ch)
        count += 1

if count != 0:
    avg = total / count
    print("Sum of digits:", total)
    print("Average of digits:", avg)
else:
    print("No digits found")












    
