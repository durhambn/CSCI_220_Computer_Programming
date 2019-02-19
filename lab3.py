## Brandi Durham
## lab3.py

from graphics import *

#Calculate the average of a group of numbers per assignment instructions
def average():
    print("Finds average")
    numGrades = eval(input("How many grades? "))
    total = 0
    for i in range(numGrades):
        stuGrade = eval(input("Enter your grade on HW"+str(i+1) +": "))
        total = total + stuGrade
    avgGrade = total / numGrades
    print("The average is: ",avgGrade)


def fibonacci():
    print("Shows a Fibonacci sequence")
    nthNum = eval(input("What is the n value? "))
    first = 0
    second = 1
    for i in range(nthNum):
        total = first + second
        print(first)
        first = second
        second = total
    

def newton():
    print("Calculates a square root")
    num = eval(input("Enter number to find square of: "))
    improve = eval(input("Enter number of times to improve approximation: "))
    approx = num /2
    print("Square root of", num, "is: ")
    for i in range(improve):
        approx = (approx + (num / approx)) / 2
    print(approx)


def buildHouse():
    winWidth = 300
    winHeight = 400
    win = GraphWin("House", winWidth, winHeight)
    win.setBackground("blue")
    
    center = Point(winWidth//2, winHeight//2)
    
    houseBottom = Rectangle(Point (100,300), Point (200,200))
    houseBottom.setFill("white")
    houseBottom.draw(win)

    houseTop = Polygon(Point(100,200),Point(200,200),Point(150,100))
    houseTop.setFill("brown")
    houseTop.draw(win)


def sequence():
    print("Writes sequence")
    numTerms = eval(input("Enter number of terms in sequence: "))
    total = 1
    for i in range(numTerms):
        total = total + (i%2) * 2
        print(total)
    
    
    
    
          

#Example graphics program
def makeCircle():
    #creates the window
    winWidth = 300
    winHeight = 400
    win = GraphWin("Click a point", winWidth, winHeight)
    win.setBackground("yellow")

    #creates a Point object that is centered in the window
    center = Point(winWidth//2, winHeight//2)

    #draws a blue circle around center point
    ball = Circle(center, 20)
    ball.setFill("blue")
    ball.draw(win)
        
    #creates and displays instructions
    instructPoint = Point(winWidth//2, winHeight - 10)
    instructions = Text(instructPoint, "Click window to close.")
    instructions.draw(win)

    #Allows the user to click the window and then closes window
    clickPt = win.getMouse()
    win.close()
    
def main():
    average()
    #fibonacci()
    #newton()
    #sequence()
    #pi()
