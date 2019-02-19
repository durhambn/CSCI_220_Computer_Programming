# CSCI 220L - Lab 10 Solutions
#
# Name 1:Evan Tanner
#
# Name 2:Brandi Durham
#
import random

def calculateSum(value, numIterations):
    i = 0
    number = 0
    while i < numIterations:
        i += 1

        number += float(value)
    return number

def areEqual(num1,num2):
    epsilon = .0001
    if abs(num1 - num2) < epsilon:
        return True
    
    else:
        return False

def goodInput():
    number = eval(input("Number: "))
    while (number < 1 or number > 10) and number != -1 and number <= 50:
        print("Number entered has to be between 1-10, -1, or greater than 50")
        number = eval(input("Number: "))
    return number

def numDigits():
    number = 1
    while number > 0:
        numDiv = 0
        number = eval(input("Number: "))
        num = number
        while num > 0:
            num = num // 10
            numDiv += 1
        print(numDiv)

def hiLoGame():
    randomInt = random.randint(1,100)
    guess = eval(input("Enter your guess: "))
    total = 1
    while guess != randomInt and total < 7:
        if guess > randomInt:
            print("Too high")
        if guess < randomInt:
            print("Too low")
        guess = eval(input("Enter your guess: "))
        total += 1
    if guess == randomInt:
        print("You win in " + str(total) + " guesses.")
    else:
        print("Sorry you lose. The number was " + str(randomInt))

        
        
    
        
        
        
    


def main():
##    result = calculateSum(.1, 10)
##    equals = areEqual(1.0,result)
##    if equals:
##            print("The two numbers are equal")
##    else:
##            print("The two numbers are not equal")
##    answer = goodInput()
##    print(answer)
##
##    numDigits()
    hiLoGame()

    
        
