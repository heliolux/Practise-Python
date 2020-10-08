"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
from datetime import datetime
name = input("Give me your name: ")
age = int(input("Enter your age: "))
year = (datetime.today().year)
# birthday = (100 - age) + year
birthday = ((year - age) + 100)

print("Hello {}. You are {} years old".format(name, age))
# print("Dzisiejsza data to", datetime.today().strftime('%Y-%m-%d'))
print("Will be 100 years old in the year", birthday)
