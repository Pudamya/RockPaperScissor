import random

def intro():
    print("___Game Overview___")
    print("First, you need to select a on from Rock, Paper and Scissor")
    print("At the same time, computer also select one from them.")
    print("You have 10 scores at the begining and you loose two scores for each lose and gain 2 marks for each win. :)")
    print("Let's start the game")
    
def begin():
        words=["Rock","Paper","Scissor"]
        Uchoice=str(input("Type your choice (Rock or Paper or Scissor) : "))
        if (Uchoice=="Rock" or "rock" ) or (Uchoice=="Paper" or "paper") or (Uchoice=="Scissor" or "scissor"):
            rand=random.choice(words)
            print(rand)

def comparison(rand,Uchoice):
    if rand==Uchoice:
        print("Equal")
        print("No-Win")
        

    elif rand!=Uchoice:
        if (rand=="Rock" and Uchoice=="Scissor")or (rand=="Scissor" and Uchoice=="Paper") or (rand=="Rock" and Uchoice=="Paper"):
            score=score-2
            print("Your results are, ")
            print()
            time.sleep(3)
            print("You lost the game")
            print(" :( ")
            print("Your score is ", score)
            print()
                    
        elif (rand=="Scissor" and Uchoice=="Rock") or (rand=="Paper" and Uchoice=="Scissor") or (rand=="Paper" and Uchoice=="Rock"):
            score=score+2
            print("Your results are, ")
            print()
            time.sleep(3)
            print("You win the game")
            print(" :) ")
            print("Your score is ", score)
            print()
                    
        else:
            print("No-Win")
                    
                
    else:
        print("Invalid Input")

def leave():
    left=str(input("Do you want to play again? (Y/N) "))
    if left=="Y" or "y" or "Yes" or "yes":
        print("You can play now")
        print("****************")
        intro()
        begin()
        comparison()
        leave()
        
    elif left=="N" or "n" or "No" or "no":
        print("Thank you for playing")
        print("Have a nice day!")
        exit()
