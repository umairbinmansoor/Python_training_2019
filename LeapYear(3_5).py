# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:25:11 2019

@author: Umair Bin Mansoor
"""

# This program checks whether an year is a leap year or not

year = eval(input("Enter a year: "))
# Check if the year is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# Display the result
print(year, "is a leap year?", isLeapYear)