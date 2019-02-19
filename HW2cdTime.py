#Name: Brandi Durham
#cdTime.py
#
#Problem: Part 1 adds up the time of each song on CD.
#   Part 2 adds up the total time from multiple CD.
#Certification of Authenticuty:
#I certify that this lab is entirely my own work.

def cdTime():
    print("Calculates the total time from each song on a CD,and"
          "calculates the toal time from each CD")
    numCD = eval(input("How many CDs? "))
    totalCD = 0
    for j in range (numCD):
        total = 0
        numSong = eval(input("Enter number of songs: "))
        for i in range (numSong):
            minute, second = eval(input("Enter length of song (minute, second): "))
            timeMinute = 60 * minute
            total = total + timeMinute + second
            timeMin = total // 60
            timeSec = total % 60
        print()
        print("CD",j+1, timeMin, "min", timeSec, "sec")
        totalCD = totalCD + total
        finalHr = totalCD // 3600
        finalMin = (totalCD % 3600) // 60
        finalSec = (totalCD % 3600) % 60
        print()
    print("Total time of all CDs: ", finalHr,"hours",finalMin, "minutes", finalSec, "seconds")
        
    
