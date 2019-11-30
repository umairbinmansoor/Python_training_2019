# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:28:30 2019

@author: Umair Bin Mansoor
"""

# The program computes the Area of a circle by getting radius as input from the user

from math import pi

radius = float(input("Input the radius of the Circle: "))

Area = pi * radius * radius

print(f"The Area of the circle is {Area}")
#print("The Area of the circle is ", Area)
#print("The Area of the circle is {}".format(Area))


