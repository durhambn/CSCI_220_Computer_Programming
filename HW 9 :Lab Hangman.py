## Name: Brandi Durham
## Hangman.py
##
##
##Problem: player plays hangman with list of words picked
##randomly. Uses the graphics package. 
##
##Certification of Authenticity:
##    I certify that this lab is entirely my own work.

from random import *

def wordList(fileName):
    infile = open(fileName, "r")
    for word in infile:
        words = word.split()
        return words

def ranWord(listWords):
    ranNum = randrange(0, len(listWords)-1, 1)
    secretWord = listWords[ranNum]
    return secretWord

def correctWord(blanks):
    i = 0
    numBlanks = 0
    while numBlanks == 0 and i <len(blanks):
            if blanks[i] == "_":
                numBlanks += 1
            i+=1
    if numBlanks == 0:
        return True
    if numBlanks >0:
        return False

    
def guesses(secretWord):
    play = False
    while play == False:
        guess = []
        for letter in secretWord:
            guess.append("_")
        string = listToStr(guess)
        print(string)
        
        print()
        guessesLeft = 7
        correct = correctWord(guess)
        guessedList = []
        while guessesLeft >0 and correct == False:
            letGuess = input("Enter your guess: ")
            alreadyGuessed = False
            j=0
            for letter in guessedList:
                if letGuess == guessedList[j]:
                    alreadyGuessed = True
                j+=1
            if alreadyGuessed == False:
                guessedList.append(letGuess)
            if alreadyGuessed == True:
                print("You already picked that letter")
            print()
            i = 0
            found = False
            for letter in secretWord:
                if letGuess == secretWord[i]:
                    found = True
                    guess[i] = letGuess
                i += 1
            if found == False:
                guessesLeft -= 1
            correct = correctWord(guess)
            string = listToStr(guess)
            print(string)
            string = listToStr(guessedList)
            print("You have " +str(guessesLeft) + " guesses left")
            print("These letters have already been guessed: " +str(string))
            print()
            
        if correct == True:
            print("You are correct")
        if guessesLeft == 0:
            print("The word was " + str(secretWord))
        print()
        wantPlay = input("Do you want to play again (y/n)? ")
        if wantPlay == "y":
            play == True
        if wantPlay == "n":
            play == False

def listToStr(guess):
    string = " ".join(guess)
    return string
        
def main():
    words = wordList("wordlist.txt")

    secretWord = ranWord(words)

    guesses(secretWord)
