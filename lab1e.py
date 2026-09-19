#!/usr/bin/env python3
# Author: Darcy McLaughlin 
# Date: 16/09/26
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1e.py

#TO-DO 1:
# Create a variable called "quantity".
quantity = 5.0
# The value of "quantity" should be a decimal number of your own choice.
# Create another variable called "stock"
stock = 3.0
# The value of "stock" should also be a decimal number of your own choice.
# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module % formatting.
# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundreadths (-.--) using the module % formatting
print ("%4.2f" % (quantity * stock))
print ("%7.2f" % (quantity * stock))