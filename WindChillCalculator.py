#!/usr/bin/python3

import math

# DO NOT MODIFY any of the statements above this comment

def calculateWindchill(temp, windSpeed):
    fTemp = 35.74 + 0.6215*temp - 35.75*math.pow(windSpeed, 0.16) + 0.4275*temp*math.pow(windSpeed, 0.16)
    return fTemp

def convertTemperature(temp):
    cTemp = (temp - 32) * 5 / 9
    return cTemp
    
def displayOutput(temp, windSpeed, fTemp, cTemp):

    windF = (round(fTemp,3))
    windC = (round(cTemp,3))

    tHead1 = "Outside Temp (F)"
    tHead2 = "Wind Speed"
    tHead3 = "Wind-Chill (F)"
    tHead4 = "Wind-Chill (C)"
    tSpace = "----------------" #15
    tData1 = str(temp)
    tData2 = str(windSpeed)
    tData3 = str(windF)
    tData4 = str(windC)

    print("%-18s %-18s %-18s %s" %(tHead1, tHead2, tHead3, tHead4))
    print("%-18s %-18s %-18s %s" %(tSpace, tSpace, tSpace, tSpace))
    print("%-18s %-18s %-18s %s" %(tData1, tData2, tData3, tData4))
    
    return

def withinRange(value, min, max):
    if min <= value <= max:
        print(" ")
        inRange = 1
    else:
        print(" ")
        valueStr = str(value)
        minStr = str(min)
        maxStr = str(max)
        print("The entered value [{0}] is out of range [{1} to {2}]." .format(valueStr, minStr, maxStr))
        quit()
    return

def main():
    
    print("Hayley Lewter")
    print(" ")
    
    tempMin = int(-58)
    tempMax = int(41)
    temp = int(input("Enter the outside temperature (Fahrenheit) [-58 to 41]:"))
    
    windMin = int(2)
    windMax = int(50)
    windSpeed = int(input("Enter the wind speed [2 to 50]:"))
    
    withinRange(temp, tempMin, tempMax)
    withinRange(windSpeed, windMin, windMax)

    fTemp = calculateWindchill(temp, windSpeed)
    cTemp = convertTemperature(fTemp)

    displayOutput(temp, windSpeed, fTemp, cTemp)
    return

main() # This must be the LAST statement of the program (DO NOT INDENT)