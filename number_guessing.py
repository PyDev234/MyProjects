# Random Guessing game in python
from random import randint 

chances = 10

def rules() -> None:
    print("There will be only 5 chances for each game")
    print("You Can choose to play or exit the game after each chance")

if __name__ == '__main__':
    c = input("Do you want to play the number guessing game(Y/N) : ")
    rules()
    while chances!=0 and c.lower() == 'y':
        n = int(input("Enter a number: "))
        chances-=1
        if n==randint(0,10): 
            print("Yes won in %d chances".format(10-chances))
            break
        else:
            print("Oops! Wrong Answer",f"Chances left: {chances}", sep = "\t\t")
            c = input("Try Again(Y/N) :")
    else:
        if chances==0: print("All the chances are over\nCome Again next time")
        else: print("Program terminating!")