# Practice Python
# Character Input 
# Exercise 1
# Instructions: Create a program that asks the user to enter their 
# name and their age. Print out a message addressed to them that tells 
# them the year that they will turn 100 years old. Note: for this exercise,
# the expectation is that you explicitly write out the year (and therefore 
# be out of date the next year).

# Extras:

# 1) Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations 
# exists in Python)
# 2) Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# My Solution
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
year = 2023 + (100 - int(age))

prompt = f'Hi, {name}! You will be 100 years onld in {year}'
prompt2 = f'\nHi, {name}! You will be 100 years onld in {year}'
print(prompt)

num = int(input("Enter A Number: "))
if num > 0:
    for i in range(num):
        print(prompt2)
