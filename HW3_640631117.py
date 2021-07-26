# -*- coding: utf-8 -*-
"""
Function: Stick picking game with a intelligence AI player
Author:Chanwit Chanton
Date: July, 26 2021
"""
import random
number=int(input("How many sticks in the pile: "))
print("There are {} sticks in the pile.Don't pick the last stick!, if you no need to loss this game.".format(number))
name = input("What is your name: ")
while number > 0: 
   out=int(input("{},How many sticks you will take (1 or 2): ".format(name)))
   if (out == 1 or out == 2) and number-out > 0: 
      number-=out
      turnbot = 1 #Turn of bot is on
      print("There are {} sticks left.".format(number))  #Bot turn part
      if turnbot == 1 and number%3==2:
          out=1 #Make Bot always becomes the winner
          number-=out
          turnbot = 0 #Turn of bot is off
          print('I smart computer, takes:{},There are {} sticks left.'.format(out,number))
      elif turnbot == 1 and number%3==0:
          out = 2 #Make Bot always becomes the winner
          number-=out
          turnbot = 0 #Turn of bot is off
          print('I smart computer, takes:{},There are {} sticks left.'.format(out,number))
      elif turnbot == 1 and number == 1:
          out = 1 #Make Bot become the loser following the rule of game
          number-=out
          turnbot = 0 #Turn of bot is off
          print("I smart computer takes the last stick." )
      elif turnbot == 1 and number%3 ==1:
          out = random.randint(1, 2) #in this senario bot are always loser
          number-=out
          turnbot = 0 #Turn of bot is off
          print('I smart computer, takes:{},There are {} sticks left.'.format(out,number)) 
   else:
       if (out == 1 or out == 2) and number-out == 0 :
           number-=out 
           turnbot = 1 #Turn of bot is on
           print("{},you take the last stick.".format(name))
       else: 
           if (out == 1 or out == 2) and number-out == -1: #Not enough stick left
               print("Oh no! There is only one stick left,Just pick the last one and cry.")
           else: #Pick with wrong amount condition
               print("You need to pick at least one stick each your turn, but not over two.") 
if turnbot == 0: #End at bot
        print("{},wins! I smart computer wanna cry.".format(name))
else: #End at human
        print("I smart computer wins! {},You lose bot!".format(name))
 



