#hangman Game

#------------- == []
#win
#or Reduce the turns
#if losses the man dies

#Algorith
#develop the intereface
#predefine list
#instruction
#check the enter word if right enter the empty list then draw a figure
#reduce the turns 
#generate the figure
import random
def hangman():

    word = random.choice(["tree","superman","tiger","superman","thor","avengers","pugger","kunal","lion","savewater"])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""
        
        if main == word:
            print(main)
            print("You win")
            break

        print("Guess the word", main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Invalid character")
            guess = input()
        if guess not in word:
            turns = turns -1 
            if turns == 9:
                print("9 turns left")
                print(" ------------- ")
                print("        0       ")
            if turns == 8:
                print("8 turns left")
                print(" ------------- ")
                print("        0       ")
                print("        |       ")
            if turns == 7:
                print("7 turns left")
                print(" ------------- ")
                print("        0       ")
                print("        |       ")
                print("       /        ")
            if turns == 6:
                print("6 turns left")
                print(" ------------- ")
                print("        0       ")
                print("        |       ")
                print("       / \      ")
            if turns == 5:
                print("5 turns left")
                print(" ------------- ")
                print("      \ 0       ")
                print("        |       ")
                print("       / \     ")
            if turns == 4:
                print("4 turns left")
                print(" ------------- ")
                print("      \ 0 /     ")
                print("        |       ")
                print("       / \     ")
            if turns == 3:
                print("3 turns left")
                print(" ------------- ")
                print("      \ 0_/___     ")
                print("        |       ")
                print("       / \     ")
            if turns == 2:
                print("9 turns left")
                print(" ------------- ")
                print("      \ 0_/___ |")
                print("        |       ")
                print("       / \     ")
            if turns == 1:
                print("Our last chance")
                print(" ------------- ")
                print("      \ 0_/___ |")
                print("        |      |")
                print("       / \      ")

            if turns == 0:
                print("You loose")
                print("You let the kind man die")
                print("      \ 0_/___ |")
                print("        |      |")
                print("       / \     |")
                break

name = input("enter ur name")
print("Welcome", name)
print("***********************")
print("try to guess the words in 10 trys")
hangman()



