
## lab2.py
## Purpose: Solves problems assigned in Lab 2
## Name: Brandi Durham 

import math

def helloWorld():
    print("Hello, world!")

def sumOfThrees():
    print("This function sums multiples of three.")
    upperBound = eval(input("Enter Upper Bound: "))
    print()
    total = 0
    for i in range (upperBound // 3):
        term = 3 * i + 3
        total = total + term
        print("When the term is:", term, ",the total is: .", total)
        print()

def multiplicationTable():
    print("Multiplication Table")
    total = 0
    for i in range ( 1, 13 ):
        print( i , end = " ")
    print()
    for j in range(1,13):
        
    
        for i in range (1, 13):
            print( i*j, end = " ")
        print()
    #for i in range(1,13):
##        print( i * 2, end = " ")
##    print()
##    for i in range(1,13):
##        print( i * 3, end = " ")
        




def triangleArea():
    print("Calculates area of a triangle")
    sa = eval(input("Enter side A length: "))
    sb = eval(input("Enter side B length: "))
    sc = eval(input("Enter side C length: "))                         
    side = (sa + sb + sc)/2
    area = math.sqrt (side*(side-sa)*(side-sb)*(side-sc))
    print("Area: ",area)

def sumSquares():
    print("Calculates sum of the squares of the given range")
    lowerRange = eval(input("Enter lower range: "))
    upperRange = eval(input("Enter upper range: "))
    total = 0
    for i in range(lowerRange, upperRange+1):
        term = i ** 2
        total = total + term
    print("Total: ", total)


def power():
    print("Calculates a number to a power")
    base = eval(input("Enter the base: "))
    power = eval(input("Enter the exponent: "))
    total = 1
    for i in range(power):
        total = total * base
    print(base, "^", power,"=", total)

    
    
                 
                  
    
    
    
                      
    


#Type each function here then call the function from main() below.
#Once the function is working correctly, you can put a comment symbol
#in front of the call in main() so that you don't have to see it run over
#and over.  An example helloWorld function is above with a commented out
#call to the working function below.

def main():
    #helloWorld()  
    sumOfThrees()





    
    

    

    

