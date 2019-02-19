## Name: Brandi Durham
## Hangman.py
##
##
##Problem: player plays hangman with list of words picked
##randomly. Uses the graphics package. 
##
##Certification of Authenticity:
##    I certify that this lab is entirely my own work.

from graphics import * 
from random import *
import time

def wordList(fileName):
    infile = open(fileName, "r")
    words = []
    for line in infile:
        list1 = line.split("\n")
        words.append(list1[0])
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
    winHeight = 400
    winWidth = 400

    win = GraphWin("Hangman", winWidth, winHeight)

    background = Line(Point(100, 300), Point(300, 300))
    background.draw(win)

    back2 = Line(Point(300, 300), Point(300, 100))
    back2.draw(win)

    back3 = Line(Point(300, 100), Point(200, 100))
    back3.draw(win)

    back4 = Line(Point(200, 100), Point(200, 150))
  

    head = Circle(Point(200, 170), 20)
  

    body = Line(Point(200, 190), Point(200, 260))


    arm1 = Line(Point(200, 220), Point(175, 190))


    arm2 = Line(Point(200, 220), Point(225, 190))


    leg1 = Line(Point(200, 260), Point(175, 290))
  

    leg2 = Line(Point(200, 260), Point(225, 290))

    wrongLetter = [leg2, leg1, arm2, arm1, body, head, back4]
   

    instGuess = Text(Point(150, 375), "Enter your guess, then click in window:")
    instGuess.draw(win)
    text3 = Text(Point(200, 340), "Gueses left: ")
    text3.draw(win)
    text4 = Text(Point(200, 355), "These letters have already been guessed:")
    text4.draw(win)


    play = True
    while play == True:
        guessText = Text(Point(200, 320), "")
        guessText.draw(win)

        guessesLeftText = Text(Point(250, 340), "")
        guessesLeftText.draw(win)
        guessedLetters = Text(Point(350, 355), "")
        guessedLetters.draw(win)
        guess = []
        for letter in secretWord:
            guess.append("_")
        string = listToStr(guess)
        guessText.setText(string)
        
        guessesLeft = 7
        correct = correctWord(guess)
        guessedList = []

        while guessesLeft >0 and correct == False:

            entry1 = Entry(Point(280, 375), 1)
            entry1.draw(win)
            win.getMouse()
            letGuess = entry1.getText()
            
            alreadyGuessed = False
            j=0
            for letter in guessedList:
                if letGuess == guessedList[j]:
                    alreadyGuessed = True
                j+=1
            if alreadyGuessed == False:
                guessedList.append(letGuess)
            if alreadyGuessed == True:
                alreadyPicked = Text(Point(200, 390), "You already picked that letter")
                alreadyPicked.draw(win)
                time.sleep(.5)
                alreadyPicked.undraw()
            i = 0
            found = False
            for letter in secretWord:
                if letGuess == secretWord[i]:
                    found = True
                    guess[i] = letGuess
                i += 1
            if found == False and alreadyGuessed == False:
                guessesLeft -= 1
                wrongLetter[guessesLeft].draw(win)
            correct = correctWord(guess)
            string = listToStr(guess)
            guessText.setText(str(string))
            string = listToStr(guessedList)
            guessesLeftText.setText(str(guessesLeft))
            guessedLetters.setText(str(string))

            
        if correct == True:
            correctText = Text(Point(200, 50), "You are correct")
            correctText.draw(win)
        if guessesLeft == 0:
            lostText = Text(Point(200, 50), "You lose.\n The word was " +str(secretWord))
            lostText.draw(win)
            

        entry2 = Entry(Point(290, 70), 1)
        entry2.draw(win)
        wantPlayInst = Text(Point(200, 70), "Do you want to play again (y/n)? ")
        wantPlayInst.draw(win)
        win.getMouse()
        wantPlay = entry2.getText()
        if wantPlay == "y":
            play = True
            guessText.undraw()
            guessesLeftText.undraw()
            guessedLetters.undraw()
            wrongLetter[0].undraw()
            wrongLetter[1].undraw()
            wrongLetter[2].undraw()
            wrongLetter[3].undraw()
            wrongLetter[4].undraw()
            wrongLetter[5].undraw()
            wrongLetter[6].undraw()
            entry2.undraw()
            wantPlayInst.undraw()
            if correct == True:
                correctText.undraw()
            if guessesLeft == 0:
                lostText.undraw()
            words = wordList("wordlist.txt")
            secretWord = ranWord(words)
        if wantPlay == "n":
            play = False
    inst = Text(Point(200, 85), "Click to close")
    inst.draw(win)
    win.getMouse()
    win.close()
    
def listToStr(guess):
    string = " ".join(guess)
    return string
        
def main():
    words = wordList("wordlist.txt")

    secretWord = ranWord(words)

    guesses(secretWord)


