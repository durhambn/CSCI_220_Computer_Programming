## Lab1.py
## CSCI 220L
## Brandi Durham

import math

#Simple function to print statement to user
def main():
    print("Programming is fun, but it is not a spectator sport.")

    print("I look forward to learning to control this computer through programming!")

    print("Hello, world") #string
    print("Hello", "world") #two stings separated by a comma
    print("2" + "3") #two strings being added
    print(2+3) #integers being added 
    print(2*3) #integers being multiplied
    print("2" *3) #string '2' 3 times
    


#Calculates the area of a rectangle
def calcRectArea ():
    print ("Calculates area of a rectangle")
    length = eval(input("Enter Length: "))
    width = eval(input("Enter Length: "))
    area = length * width
    print ("Area:" , area)
    print()

#Calculates the volume of a cylinder
def calcCylinderVolume ():
    print ("Calculates volume of a cylinder")
    PI = math.pi
    radius = eval(input("Enter radius: "))
    hight = eval(input("Enter hight: "))
    area = PI * radius**2 * hight
    print ("Area: ", area)



#Compute the cost of shipping a coffee order
def coffee ():
    print ("Calculates the cost of shipping a coffee order")
    pounds = eval(input("Enter number of pounds of Coffee: "))
    coffee = 10.50
    shipping = .86
    fixed = 1.50
    cost = (pounds * coffee) + (pounds * shipping) + fixed
    print ("Order costs: ", cost)

    

#Kilometers to miles conversion
def kilometersToMiles ():
    print ("Converts Kilometers to miles")
    kilometers = eval(input("Enter kilometers: "))
    KM_TO_MILES = 1.61
    miles = kilometers/ KM_TO_MILES
    print ("Miles: ",miles)
    
                      
           
                  
    
                  
    
