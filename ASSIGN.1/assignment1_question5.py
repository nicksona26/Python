#question 5
degrees=float(input("Enter a temperature between -58 and 41 degrees fahrenheit: "))
speed=float(input("Enter a wind speed in miles per hour that is greater than or equal to 2: "))
windchill = 35.74+0.6215*degrees-35.75*speed**0.16+0.4275*degrees*speed**0.16
print("The wind chill index is {0:.2f}".format(windchill))

