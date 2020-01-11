# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 22:27:01 2020

@author: Umair Bin Mansoor
"""

#Example 1
num_list1 = [y for y in range(100) if y % 10 == 0]
print(num_list1) #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#Example 2
num_list2 = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list2) #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#Example 3
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj) #['Even','Odd','Even','Odd','Even','Odd','Even','Odd','Even','Odd']
