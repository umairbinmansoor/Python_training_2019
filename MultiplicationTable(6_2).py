# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:57:02 2020

@author: Umair Bin Mansoor
"""

# The program presents a program that uses nested for loops to display a multiplication table.

print(" Multiplication Table")
# Display the number title
print(" |", end = '')
for j in range(1, 10):
    print(" ", j, end = '')
print() # Jump to the new line
print("——————————————————————————————————————————")

# Display table body
for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10):
        # Display the product and align properly
        print(format(i * j, "4d"), end = '')
    print() # Jump to the new line