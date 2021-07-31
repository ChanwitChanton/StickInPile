# -*- coding: utf-8 -*-
"""
Function: List Comprehension 
Author:Chanwit Chanton
Date: August, 1 2021
"""

sub_string = input("Enter four non negative integers separated by comma (,) Ex. 1,2,3,4 : ")
string_list=sub_string.split(",") # Split each string by comma (,)
import itertools  
arr = itertools.permutations(string_list) #To use permutation to arrange pattern in string_list
largest_number = [] # To create a list to contain strings as the list of candidate largest number
for i in arr:
    pattern_number = [] # To create a list to contain the arranged patterns of candidated largest number
    string_connext = '' # To merge all of the arranged patterns of candidated largest number, and also change list to string 
    for p in i:
        pattern_number.append(str(p)) # To generate the arranged patterns in list type 
    for s in pattern_number:
        string_connext += s # To merge each list as pattern in string type
        largest_number.append(string_connext) # To collect the arranged patterns of candidated largest number in string type  
print("The largest formed number is :", max(largest_number)) 