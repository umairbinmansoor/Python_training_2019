# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:25:05 2019

@author: Umair Bin Mansoor
"""

# This program explains Tuple usage

tuple1 = ("green", "red", "blue") # Create a tuple
print(tuple1)
tuple2 = tuple([7, 1, 2, 23, 4, 5]) # Create a tuple from a list
print(tuple2)
print("length is", len(tuple2)) # Use function len use functions
print("max is", max(tuple2)) # Use max
print("min is", min(tuple2)) # Use min
print("sum is", sum(tuple2)) # Use sum
print("The first element is", tuple2[0]) # Use index operator
tuple3 = tuple1 + tuple2 # Combine two tuples
print(tuple3)
tuple3 = 2 * tuple1 # Duplicate a tuple
print(tuple3)
print(tuple2[2 : 4]) # Slicing operator
print(tuple1[-1])
print(2 in tuple2) # in operator
list1 = list(tuple2) # Obtain a list from a tuple
list1.sort()
tuple4 = tuple(list1)
tuple5 = tuple(list1)
print(tuple4)
print(tuple4 == tuple5) # Compare two tuples