##Name: Brandi Durham
##weightedAverage.py
##
##problem: Calculates a persons avarage and the class average
##from a set of grades from a file
##
##Certification of Authenticity:
##    I certify that this lab is entirely my own work.
   

def weightedAverage():
    #ask user for name of file of grades
    fileName = input("Enter name of file: ")
    infile = open(fileName, "r")
    #compute each students average and print
    totalAvg = 0
    numOfPpl = 0
    for line in infile:
        parts = line.split()
        name = parts[:2]
        firstLast = " ".join(name)
        gradeAndAvg = parts[2:]
        #multiply weight and grade and add each together and / by 100
        weight = gradeAndAvg[::2]
        grades = gradeAndAvg[1::2]
        total = 0
        totalGrades = 0
        for i in range(len(weight)):
            #weight times average
            wXa = eval(weight[total]) * eval(grades[total])
            total += 1
            totalGrades += wXa
        average = totalGrades / 100
        print(firstLast +"'s average: " + str(average))
        totalAvg += average
        numOfPpl += 1
        #track num of people
    print()
    #class average = total of all grades / num of people
    classAvg = totalAvg / numOfPpl
    print("Class average: ", round(classAvg,1))
    #rounds the class average to one decimal place
    
    
