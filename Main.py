import random
import sys
import RockPaperScissor
import time

score=10
welcome="Welcome to Rock Paper Scissor Game"
print(welcome.center(44,"*"))
print()

name=str(input("Please enter your name : "))
print()
print("Hi",name)
print()


RockPaperScissor.intro()
RockPaperScissor.begin()
rand,Uchoice=RockPaperScissor.begin()
RockPaperScissor.comparison(rand,Uchoice)
RockPaperScissor.leave()
