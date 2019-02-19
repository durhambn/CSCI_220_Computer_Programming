# CSCI 220L - Lab 8 Solutions
#
# Name 1:Brandi Durham
#
# Name 2:Michael Preddy
#

def formatPractice():
    print("It's raining {1} and {0}.".format("cats","dogs"))
    print("{0:04.2f}  {1:04.3f}".format(2.3, .4567))
    print("Time left {0:02}:{1:05.2f}".format(3,7.4589))
    print("{0} {1}: {2:5.2f}".format("Steph", "Curry", 43.75432))

def encode(ch, key):
    final = " "
    for i in range(len(ch)):
        newCh = chr(ord(ch[i]) + key)
        final += newCh
    return final

def encodeBetter(ch, key):
    final=" "
    for i in range(len(ch)):
        final += chr(((ord(ch[i]) - ord("a") + key)%26) + ord("a"))
    return final

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10    

#function to test code in problem 4.  Do not run
#until addTen() is written
def testTens():
    values = [5, 2, -3]
    print(values)
    addTen(values)
    print(values)

def squareEach(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]**2

def sumOfSquares():
    values= [5,2,-3]
    print(values)
    squareEach(values)
    print(values)
    print(sumList(values))
    listOfStr = ["3","5.7", "2"]
    toNumbers(listOfStr)
    print(listOfStr)
    

def sumList(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total

def toNumbers(strList):
    for i in range(len(strList)):
         strList[i] = (eval(strList[i]))
    
def main():

    final = encode("hello", 3)
    print("Cipher of hello is ", str(final))

    final = encodeBetter("xray", 3)
    print(final)




