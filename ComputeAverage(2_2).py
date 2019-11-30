# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:04:00 2019

@author: Umair Bin Mansoor
"""

# This program calculates the average of 3 numbers provided by the user

number1 = eval(input("Enter the first number: "))
number2 = eval(input("Enter the second number: "))
number3 = eval(input("Enter the third number: "))

# Compute average
average = (number1 + number2 + number3) / 3

# Display result
print("The average of", number1,",", number2,",", number3, "is", average)
#print(f"The average of {number1}, {number2}, {number3} is {average}")
#