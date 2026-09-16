#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 16/09/26
# Purpose: Use arithmetic in python.
# Usage: python3 lab1b.py

# TO-DO 1:
#	Create a variable called "num1", take its value from user.
num1 = input ("Enter a Number: ")
#	Create another variable called "num2" and take its value from user. 
num2 = input ("Enter a second Number: ")
# Convert the values to integers using int() function
print (type(num1))
print (type(num2))
num1 = int(num1)
num2 = int (num2)


# TO-DO 2:
# Perform all arithmetic oeprations as outlined in the description in README.md file, and print in the required format.
print (num1 + num2)
print (num1 - num2)
print (num1 * num2)
print (num1 ** num2)
print (num1 / num2)
print (num1 // num2)
print (num1 & num2)