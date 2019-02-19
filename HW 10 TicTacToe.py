## Name: Brandi Durham
## TicTacToe.py
##
##
##Problem: Players play tic-tac-toe 
##
##Certification of Authenticity:
##    I certify that this lab is entirely my own work.




def board():
    listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return listNum

def drawBoard(listNum):
    print(str(listNum[0]) +str("|")+ str(listNum[1]) + str("|")+ str(listNum[2]))
    print("------")
    print(str(listNum[3]) +str("|")+ str(listNum[4]) + str("|")+ str(listNum[5]))
    print("------")
    print(str(listNum[6]) +str("|")+ str(listNum[7]) + str("|")+ str(listNum[8]))

def gameWon(listNum):
    if listNum[0] == listNum[1] == listNum[2]:
        return True
    if listNum[3] == listNum[4] == listNum[5]:
        return True
    if listNum[6] == listNum[7] == listNum[8]:
        return True
    if listNum[0] == listNum[3] == listNum[6]:
        return True
    if listNum[1] == listNum[4] == listNum[7]:
        return True
    if listNum[2] == listNum[5] == listNum[8]:
        return True
    if listNum[0] == listNum[4] == listNum[8]:
        return True
    if listNum[2] == listNum[4] == listNum[6]:
        return True

    
def startGame(listNum):
    attempt = 0
    gameOver = False
    while attempt < 8 and gameOver == False:
        spot1 = eval(input("Player 1, Enter spot on board: "))
        print()
        while spot1 >= 10 or spot1 <= 0:
            spot1 = eval(input("Not valid position, Enter position: "))
        if listNum[spot1-1] != "X" and listNum[spot1-1] != "O":
            listNum[spot1-1] = "X"
            drawBoard(listNum)
            attempt +=1
        else:
            print("Not a valid position")
            spot1 = eval(input("Enter position: "))
            while listNum[spot1-1] == "X" or listNum[spot1-1] == "O":
                spot1 = eval(input("Enter different position: "))
            listNum[spot1-1] = "X"
            drawBoard(listNum)
            attempt +=1
        if gameWon(listNum) == True:
            gameOver = True
            if listNum[spot1-1] =="X":
                print("Player 1 wins")
            if listNum[spot1-1] =="O":
                print("Player 2 wins")
        print()
        if gameOver !=True:
            spot2 = eval(input("Player 2, Enter spot on board: "))
            print()
            while spot2 >= 10 or spot2 < 0:
                spot1 = eval(input("Not valid position, Enter position: "))
            if listNum[spot2-1] != "X" and listNum[spot2-1] != "O":
                listNum[spot2-1] = "O"
                drawBoard(listNum)
                attempt += 1
            else:
                print("Not a valid position")
                spot2 = eval(input("Enter position: "))
                while listNum[spot2-1] == "X" or listNum[spot2-1] == "O":
                    spot2 = eval(input("Enter different position: "))
                listNum[spot2-1] = "O"
                drawBoard(listNum)
                attempt +=1
            if gameWon(listNum) == True:
                gameOver = True
                if listNum[spot2-1] =="X":
                    print("Player 1 wins")
                if listNum[spot2-1] =="O":
                    print("Player 2 wins")
            print()
       
    if attempt == 8:
        spot = eval(input("Player 1, Enter your desired spot on board: "))
        if listNum[spot-1] != "X" and listNum[spot-1] != "O":
            listNum[spot-1] = "X"
            drawBoard(listNum)
    if gameOver == False:
        print("It's a tie")
    return listNum
        
            
    


def main():
    listNum = board()
    drawBoard(listNum)
    print()
    listNum = startGame(listNum)
    didWin = gameWon(listNum)
    
    
    
              
