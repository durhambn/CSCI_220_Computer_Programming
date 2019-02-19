## Name: Brandi Durham
## SalesPerson.py
##
##
##Problem: make a class object, SalesPerson and SalesForce
##
##Certification of Authenticity:
##    I certify that this lab is entirely my own work.

class SalesPerson:
    def __init__(self, idNum, name):
        self.idNum = idNum
        self.name = name
        self.listOfSales = []

    def getidNum(self):
        return self.idNum

    def getName(self):
        return self.name

    def setName(self, strName):
        self.name = str(strName)

    def enterSale(self, aSale):
        if type(aSale) == float or type(aSale) == int:
            self.listOfSales.append(aSale)
            
    def totalSales(self):
        total = 0
        for num in self.listOfSales:
            total +=num
        return total

    def getSales(self):
        return self.listOfSales

    def metQuota(self, quota):
        if self.totalSales() >= quota:
            return True
        else:
            return False
        
    def compareTo(self, otherPerson):
        if self.totalSales() < otherPerson:
            return -1
        if self.totalSales() == otherPerson:
            return 0
        if self.totalSales() > otherPerson:
            return 1

    def __str__(self):
        rtnStr = "ID: " +str(self.idNum)
        rtnStr+=  "\nName: " + str(self.name)
        rtnStr+=  "\nTotal Sales: " +str(self.totalSales())
        return rtnStr

class SalesForce:
    def __init__(self):
        self.salesPersonList = []

    def addData(self, fileName):
        infile = open(str(fileName), "r")
        for line in infile:
            parts = line.split()
            personID = parts[0]
            personName = parts[1] + " " + parts[2]
            person = SalesPerson(personID, personName)
            for i in range(len(parts)-3):
                sale = eval(parts[i+3])
                person.enterSale(sale)
            i = 0
            self.salesPersonList.append(person)
            
    def quotaReport(self, quota):
        i = 0
        for i in range(len(self.salesPersonList)):
            totalSales = self.salesPersonList[i].totalSales()
            print(self.salesPersonList[i])
            print(self.salesPersonList[i].metQuota(quota))
            print()
            i += 1
            
    def topSalesPerson(self):
        salesList = []
        for i in range(len(self.salesPersonList)):
            salesList.append(self.salesPersonList[i].totalSales())
        x = 0
        top = salesList[0]
        while x < len(salesList):
            if top < salesList[x]:
                top = salesList[x]
                x += 1
            else:
                x += 1
        pos = salesList.index(top)
        return self.salesPersonList[pos]
    

    def individualSales(self, idNum):
        x = 0
        for i in range(len(self.salesPersonList)):
            num = eval(self.salesPersonList[i].getidNum())
            if num == idNum:
                print("ID: ", num, "-All Sales: ", self.salesPersonList[i].listOfSales)
                print("Total Sales: ", self.salesPersonList[i].totalSales())
                x -=1
            x +=1
        if x == len(self.salesPersonList):
            print(idNum, "-Not a valid ID number")
   
    
            
    
