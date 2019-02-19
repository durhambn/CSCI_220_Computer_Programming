##Brandi Durham
##Ashley Garrett
##observations: Linear is slower most of the time unless the
##number is at the beginning of list
##
##Pythons built in sort is faster than the selection sort. 

from graphics import*
from random import*
import math

def reverseSort(list):
    list.sort()
    list.reverse()

def findAndRemoveFirst(list, value):
    pos = list.index(value) 
    list.insert(pos, "Ashley")
##    list.remove(value)
    pos2 = list.index(value) 
    list.pop(pos2)

def readData(filename):
    infile = open(filename, "r")
    dataList = []
    for line in infile:
        list1 = line.split()
        for num in list1:
            dataList.append(eval(num))
    return dataList

def isInLinear(searchVal, values):
    i = 0
    found = False
    while i < len(values) and searchVal != values[i]:
        i += 1
    if i < len(values):
        found = True
    return found

def isInBinary(searchVal, values):
    found = False
    low = 0
    high = len(values) - 1
    mid = (low + high)//2
    while low <= high and values[mid] != searchVal:
        if searchVal< values[mid]:
            high = mid -1
        else:
            low = mid +1
        mid = (low + high)//2
    if low <= high:
        found = True
    else:
        found = False
        
    return found
        
def selectionSort(values):
    n = len(values)
    for front in range(n-1):
        minPos = front                    
        for i in range(front+1,n): 
            if values[minPos] > values[i]: 
                minPos = i                  
        teminPos = values[minPos]
        values[minPos] = values[front]
        values[front] = teminPos

def calcArea(rect):
    p1X = rect.getP1().getX()
    p1Y = rect.getP1().getY()
    p2X = rect.getP2().getX()
    p2Y = rect.getP2().getY()
    area = abs(p1X - p2X) * abs(p1Y - p2Y)
    return area
    

def rectSort(rectangles):
    areaList = []
    for rect in rectangles:
        area = calcArea(rect)
        areaList.append(area)
    print(areaList)
        
    n = len(areaList)
    for front in range(n-1):
        minPos = front                    
        for i in range(front+1,n): 
            if areaList[minPos] > areaList[i]: 
                minPos = i                  
        teminPos = areaList[minPos]
        areaList[minPos] = areaList[front]
        areaList[front] = teminPos
    return areaList

def main():
    list = [3, 5, 7, 4, 8, 3, 2]
    reverseSort(list)
    print(list)

    findAndRemoveFirst(list, 7)
    print(list)

    data = readData("dataSorted.txt")
    print(data)

    linearSearch = isInLinear(50, data)
    print(linearSearch)
    
    linearSearch = isInLinear(5, data)
    print(linearSearch)

    linearSearch = isInLinear(282, data)
    print(linearSearch)

    linearSearch2 = isInLinear(70, data)
    print(linearSearch2)

    binarySearch = isInBinary(50, data)
    print(binarySearch)

    binarySearch = isInBinary(5, data)
    print(binarySearch)

    binarySearch = isInBinary(282, data)
    print(binarySearch)

    binarySearch2 = isInBinary(70, data)
    print(binarySearch2)

    values = [15, 30, 50, 40, 10, 5, 20]
    selectionSort(values)
    print(values)

    listRects = []
    for i in range(10):
        listRects.append(Rectangle(Point(randint(0, 100), randint(0, 100)), Point(
            randint(0, 100), randint(0, 100))))

    areaList = rectSort(listRects)
    print(areaList)
  
main()
