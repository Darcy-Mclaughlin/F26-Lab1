#!/usr/bin/env python3
# Author: Darcy McLaughlin
# Date: 16/09/26
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1d.py

#TO-DO 1:
#	Create a variable called "name" and assign it the value of your name.
name = "Darcy"
# Use the string method .upper() to convert the name to upper case.
name.upper
# Create another variable called “age”, the value of “age” should be your age
age = 17
# The script, when executed, should print out "How are you yourname? Happy xxth birthday!" To print this output use .format() method. 
print ( "How are you {}? Happy {}th birthday!"  .format (name, age))

#TO-DO 2:
# Create a variable called "words".
words = "The quick brown fox jumps over the lazy dog"
# The value of words should be "The quick brown fox jumps over the lazy dog".
# Use indexing to return the first and 17th charecters of "words" to the user.
print (words [1:17])

#TO-DO 3:
# Use negative indexing to return the words "jumps" and "quick" from "words" to the user.
print (words[-39:-34])
print (words[-23:-18])

#TO-DO 4:
# Use slicing to retun everything between index 2-15 to the user.
# Print "uick brown foxs ju" from "words".
print (words[5:22])