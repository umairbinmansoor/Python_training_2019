# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 00:09:17 2019

@author: Umair Bin Mansoor
"""

import random

 # Generate random numbers
number1 = random.randint(0, 9) #Generates random numbers from 0-9
number2 = random.randrange(0, 10) #Generates random numbers from 0-9

 # Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

 # Display result
print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)