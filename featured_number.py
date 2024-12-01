'''
A featured number (something unique to this exercise) is an odd number 
that is a multiple of 7, with all of its digits occurring exactly once each. 
For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not 
(it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next 
featured number greater than the integer. Issue an error message if there
is no next featured number.

The largest possible featured number is 9876543201.
'''
'''
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
'''
'''
input: integer
output: next odd multiple of 7 with all digits occurring only once after
    input integer
rules: max featured number is 9876543201

algorithm:
1. create a test for being a featured number
    - number % 2 != 0
    - number % 7 == 0
    - convert number to string, convert to set, length should be = to # of digits
2. starting from input number:
    - add 1 and test if it meets featured number criteria
    - while it doesn't keep going
    - once it does, return featured number

'''

def next_featured(integer):

    def featured(candidate):
        return candidate % 2 != 0 and \
               candidate % 7 == 0 and \
               len(str(candidate)) == len(set(str(candidate)))
    
    candidate = integer + 1
    while not featured(candidate):
        candidate += 1
        if candidate > 9876543201:
            return "There is no possible number that fulfills those requirements."

    return candidate

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True