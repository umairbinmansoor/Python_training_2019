# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:20:52 2019

@author: Umair Bin Mansoor
"""

def assignGrade(score):
    if score >= 90.0:
        grade = 'A'
    elif score >= 80.0:
        grade = 'B'
    else:
        grade = 'F'
    return grade


score = eval(input("What is your score: "))
print(assignGrade(score))