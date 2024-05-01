#Importing modules
import random
import sys
import RockPaperScissor
import time

#Variable Initialization
score=10
name=""

#Display the title of the game
welcome="Welcome to Rock Paper Scissor Game"
print(welcome.center(44,"*"))
print()

#Taking the name of the user as an input
name=str(input("Please enter your name : "))
print()

#Printing a welcome for the user.
print("Hi",name)
print()

#Calling the functions in the RockPaperScissor module
RockPaperScissor.intro()
RockPaperScissor.begin()
rand,Uchoice=RockPaperScissor.begin()
RockPaperScissor.comparison(rand,Uchoice)
RockPaperScissor.leave()
