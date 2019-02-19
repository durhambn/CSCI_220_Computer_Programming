# Name: Brandi Durham
## jumpingJack.py
##
##
##Problem: Stick figure does jumping jacks when person
##clicks start, stops when person hits stop, ends program
##when user clicks quit.
##
##Certification of Authenticity:
##    I certify that this lab is entirely my own work.

from graphics import *
import time

def wasClicked(pt, rect):
    if pt == None:
        return False
    else:
        rectP1 = rect.getP1()
        rP1X = rectP1.getX()
        rP1Y = rectP1.getY()
        
        rectP2 = rect.getP2()
        rP2X = rectP2.getX()
        rP2Y = rectP2.getY()
        
        ptX = pt.getX()
        ptY = pt.getY()

        if ptX >= rP1X and ptX <= rP2X and ptY >= rP1Y and ptY <= rP2Y:
            return True
        else:
            return False
        
 

def main():
    winHeight = 400
    winWidth = 400

    win = GraphWin("Jumping Jack", winWidth, winHeight)

    jackBody= Line(Point(200,150), Point(200, 250))
    jackBody.draw(win)

    jackHead = Circle(Point(200, 125), 25)
    jackHead.draw(win)

    jackArm1 = Line(Point(200, 200), Point(250, 150))
    jackArm1.draw(win)

    jackArm1Move = Line(Point(200, 200), Point(245, 125))

    jackArm2 = Line(Point(200, 200), Point(150, 150))
    jackArm2.draw(win)

    jackArm2Move = Line(Point(200, 200), Point(145, 125))

    jackLeg1 = Line(Point(200, 250), Point(250, 300))
    jackLeg1.draw(win)

    jackLeg1Move = Line(Point(200,250), Point(215,300))

    jackLeg2 = Line(Point(200, 250), Point(150, 300))
    jackLeg2.draw(win)

    jackLeg2Move = Line(Point(200,250), Point(185,300))

    startBox = Rectangle(Point(75, 325), Point(125, 375))
    startBox.draw(win)
    
    startText = Text(Point(100, 350), "Start")
    startText.draw(win)

    stopBox = Rectangle(Point(175, 325), Point(225, 375))
    stopBox.draw(win)

    stopText = Text(Point(200, 350), "Stop")
    stopText.draw(win)

    quitBox = Rectangle(Point(275, 325), Point(325, 375))
    quitBox.draw(win)

    quitText = Text(Point(300, 350), "Quit")
    quitText.draw(win)

    instructions = Text(Point(200, 50), "To start click Start button,\n"
                        "to stop click Stop button,\n to quit click Quit button")
    instructions.draw(win)

    click = win.getMouse()
    
    start = wasClicked(click, startBox)


    end = wasClicked(click, quitBox)
    stop = wasClicked(click, stopBox)


    while end != True:
        while stop != True:
            while start == True:
                click2 = win.checkMouse()
                end = wasClicked(click2, quitBox)
                stop = wasClicked(click2, stopBox)
                if stop == True:
                    start = False
                if end == True:
                    win.close()
                jackArm1.undraw()
                jackArm1Move.draw(win)
                
                jackArm2.undraw()
                jackArm2Move.draw(win)

                jackLeg1.undraw()
                jackLeg1Move.draw(win)

                jackLeg2.undraw()
                jackLeg2Move.draw(win)
                
                time.sleep(.5)
                
                jackArm1Move.undraw()
                jackArm1.draw(win)

                jackArm2Move.undraw()
                jackArm2.draw(win)

                jackLeg1Move.undraw()
                jackLeg1.draw(win)

                jackLeg2Move.undraw()
                jackLeg2.draw(win)
                
                time.sleep(.5)
        click2 = win.checkMouse()
        end = wasClicked(click2, quitBox)
        start = wasClicked(click2, startBox)
        if start == True:
            stop = False
        if end == True:
             win.close()
        
                
                
               
    win.close()

    
