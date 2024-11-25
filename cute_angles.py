'''
Write a function that takes a floating point number 
representing an angle between 0 and 360 degrees and 
returns a string representing that angle in degrees, 
minutes, and seconds. You should use a degree symbol (°) 
to represent degrees, a single quote (') to represent minutes, 
and a double quote (") to represent seconds. There are 60 minutes 
in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:
DEGREE = "\u00B0"
'''
'''
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
'''

'''
P:
input: float representing an angle
output: string with degrees, minutes and seconds
-implicit: only two digits for minutes and seconds, 3 for degrees
- angle is whatever comes before decimal
- minutes/seconds come from after decimal

Algorithm:
2. separate by . -> list
3. list index 1 is degrees, save
4. list index 2 is minutes and seconds
    - to convert to minutes and seconds:
    - multiply index 2 by .6, convert to string, save first two digits as minutes
    - for after decimal, multiply by .6, 
'''

def dms(angle):
    DEGREE = "\u00B0"

    degrees = int(angle // 1)
    minutes_seconds = (angle - degrees) * 60
    minutes = int(minutes_seconds // 1)
    seconds = int((minutes_seconds - minutes) * 60 // 1)

    return (f"{degrees}{DEGREE}{minutes:02}'{seconds:02}\"")

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")


number = 1.34
formatted = f"{number:08.2f}"
print(formatted)  # Output: 00001.34

number = 1.34
formatted = f"{number:06.2}"
print(formatted)  # Output: 00001.34
