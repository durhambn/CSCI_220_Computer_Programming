# Lab6.py
# Name 1:Evan Tanner
# Name 2:Brandi Durham

def nameReverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("What is your name? ")
    name = name.split()
    firstName = name[0]
    lastName = name[1]
    print("The name reversed is", lastName + ", " + firstName)

def companyName():
    web = input("Enter website: ")
    web = web.split(".")
    comName = web[1]
    print("Company Name is ", comName)

def initials():
    numOfStud = eval(input("How many students? "))
    for i in range(numOfStud):
        firstName = input("Enter the first name of student#" + str(i+1) + ": ")
        lastName = input("Enter " + firstName + "'s last name: ")
        firstInitial = firstName[0]
        lastInitial = lastName[0]
        studIni = print(firstName + "'s initals are " + (firstInitial + lastInitial).upper())
        print()

def names():
    names = input("Enter Names separated by commas: ")
    namesFl = names.split(",")
    print("Initals are: ", end = " ")
    for names in  namesFl:
         names = names.split()
         firstName = names[0][0]
         lastName = names[1][0]
         print((firstName +lastName), end = " ")

def thirds():
    numSent = eval(input("Enter number of sentences: "))
    total = []
    for i in range (numSent):
        sent = input("Enter Sentence: ")
        for i in range(2,len(sent), 3):
            letters = sent[i]
            joinLetters = "".join(letters)
            print(joinLetters, end = " ")
        print()
    print()           

def wordCount():
    numSent = eval(input("Enter num of sentences: "))
    print()
    for i in range(numSent):
        sentence = input("Enter Sentence: ")
        wordList = sentence.split()
        print(len(wordList))
        print()

def wordAverage():
    numSent = eval(input("Enter num of sentence: "))
    for i in range(numSent):
        sent = input("Enter Sentence: ")
        wordList = sent.split()
        wordCount = len(wordList)
        sent = "".join(wordList)
        letterCount = len(sent)
 
        average = letterCount/wordCount
        print("The average of this sentence is", average)
        print()

def pigLatin():
    sent = input("Enter Sentence: ")
    sentSplit = sent.split()
    for word in sentSplit:
        print( (word[1:]+word[0]+"ay").lower(), end = " ")
        





##def main():
##    nameReverse()
##    companyName()
##    #add other function calls here
main()
