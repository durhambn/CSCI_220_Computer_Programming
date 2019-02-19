# Code compares runtimes of insertion sort and Python's built-in sort
# Author: RoxAnn H. Stalvey

from algorithms import *
from random import randint
import time

def main():
    print("Code to look at runtime for selection sort vs. Python's list sort.")
    
    numDig = 5 #number of digits to output
    
    #large list with numElements elements
    numElements = 10000
    dataSel = []
    dataPy = []
    for i in range(numElements):
        value = randint(1, numElements)
        dataSel.append(value)
        dataPy.append(value)
        
    print("\nSorting list with " + str(len(dataSel)) + " elements.\n")
    
    start = time.time()
    selectionSort(dataSel)
    end = time.time()
    print("Selection sort -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    dataPy.sort()
    end = time.time()
    print("Python's sort -> " + str(round(end - start, numDig)) + " seconds.")

main()
