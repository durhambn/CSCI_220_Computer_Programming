##Name: Brandi Durham
##mean.py
##
##problem: Calculates the RMS average and the harmonic mean
##of a group of numbers.
##
##Certification Of Authenticity:
##    I certify that this lab is entirely my own work.
##1. It will calculate the RMS average and the harmonic mean of a group of
##numbers entered by the user.
##2. Input- the number of terms and the terms.
##output- the RMS average and the harmonic mean.
##3. ask the number of terms and what the terms are.
##calulates the two different means using the formulas
##output the two different means.

import math
def mean():
    print("Calculates the RMS average and harmonic mean.")
    numTerms = eval(input("Enter number of terms: "))
    print()
    total = 0
    end = 0
    for i in range(numTerms):
        term = eval(input("Enter term: "))
        total = total + (term ** 2)
        end = end + (1/term)
    rmsAvg = math.sqrt(total / numTerms)
    harmAvg = numTerms / end
    print()
    print("The RMS average is: ", rmsAvg)
    print()
    print("The Harmonic mean is: ", harmAvg)
   
