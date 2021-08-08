# -*- coding: utf-8 -*-
"""
Function: Optimization (Opened Method)
Author:Chanwit Chanton
Date: August, 8 2021
"""

'''
Assume you open your ice cream shop, there are only two types of ice cream, vanilla and strawberry. 
When a box of ice cream is sold, you will get the benefit for $2 for vanilla ice cream and $3 for strawberry ice cream. 
To make the ice cream, the fresh milk is required. To make a box of vanilla ice cream requires 0.5 liter and strawberry ice cream requires 0.2 liter. 
You daily order 10 liters of fresh milk. 
To promote your ice cream shop, you give a doll for each ice cream box. The number of dolls, that you can give to customers, is 30 dolls per day. 
So, how many boxes of vanilla ice cream and strawberry ice cream that you would like to produce to get maximum profit ? 
 Use Python to find the answer ; provide solving explanation in PDF file
'''
#Please run the command of "pip install pulp" in cmd before run these following coding.
from pulp import *
PModel=LpProblem("Ice Cream Box Production",LpMaximize)
#Decision Variables - bi are the number of ice cream box in each flavor; i=1 as Vanilla and i=2 as Strawberry.
b1=LpVariable("b1",lowBound=0) # a number of Vanilla ice cream box which grater than equal 0.
b2=LpVariable("b2",lowBound=0) # a number of Strawberry ice cream box which grater than equal 0.
#Production Requries Constants - s1 and s2 as the amount of fresh milk which is used to produce the icecream box of Vanilla and Strawberry in each box, orderly.
#However, this is the grand opening of my ice cream shop, so I launch the campaign as "one box one doll" which means that you will get one lovely doll as D per each box of ice cream which you buy.
s1=0.5
s2=0.2
D=1
#Constraints - Production Constraint: 10 liters of fresh milk and Sale Promotion Constraint: 30 dolls per day.
PModel+=s1*b1+s2*b2<=10
PModel+=D*b1+D*b2<=30
PModel+=b1>=0
PModel+=b2>=0
#p1 and p2 as price for sale each box of Vanilla and Strawberry orderly as the alternative benefits from production
p1=2
p2=3
#Objective Function as Maximized Profit
PModel+=p1*b1+p2*b2
print(PModel)
status=PModel.solve()
vnl=int(value(b1))
stb=int(value(b2))
Max=int(value(PModel.objective))
print("The production which contains {0} boxes of Vanilla ice cream and {1} boxes of Strawberry ice cream brings us the Maximized profit at {2} $".format(vnl,stb,Max))
