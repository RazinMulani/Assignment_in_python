# Assignment 3(SET C)
# Q1) Write a python program to find word in string which contain both digit and number
'''
s = input("Enter The String")

words = s.split()
result= []

for word in words:
    has_alpha = False
    has_digit = False

    for ch in word:
        if ch.isalpha():
            has_alpha = True
        elif ch.isdigit():
            has_digit =True

    if has_alpha and has_digit:
        result.append(word)

print("Word Contaning both letters and digits")
print(result)
'''

# Q2) Write a Python program to compress a string as follows:
# Example: Input: aaabbccccd
# Output: a3b2c4d1
s1 = input("Enter The String")
compress = ""
count = 1

for i in range(len(s1)-1):
    if s1[i]== s1[i + 1]:
        count += 1
    else:
        compress += s1[i] + str(count)
        count = 1


# for tha last character
compress += s1[-1] + str(count)
print("compressed String:",compress)









