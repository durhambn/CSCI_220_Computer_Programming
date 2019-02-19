#Name: Brandi Durham
#usury.py
#Problem: This program tells the person how much
#they are going to have to pay per month, total
#amount paid over the life of the loan, and the total interest paid.
#Certification of Authenticity:
#I certify that this lab is entirely my own work.

#input initial loan amount "principal"
#input number of months
#input interest rate

#output princial payment per month
#output amount paid over the life of the loan
#output total interest paid

def usury ():
    print ("Calculates monthly payments, amount paid over"
           "the life of the loan, and total interest paid.")
    principal = eval(input("What was the initial loan amount? "))
    #input initial loan amount
    months = eval(input("How many months is the loan for? "))
    #input number of months
    interest = eval(input("What was the interest rate? "))
    #input interest rate
    rate = interest / 1200
    monPay = (principal * (rate*((1+rate)**months))) / ((1+rate)**months -1)
    #calculates monthly payment
    print()
    print ("The monthly payment is ", monPay)
    loanLifeTotal = monPay * months
    #calculates the total amount paid
    print()
    print ("The total amount paid over the life"
           "of the loan is ", loanLifeTotal)
    interestTotal = loanLifeTotal - principal
    #calculates the total interest paid
    print()
    print ("The total amount of interest paid is ", interestTotal)



