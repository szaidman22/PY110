'''
Write a function that takes a list of positive 
integers as input, multiplies all of the integers 
together, divides the result by the number of entries 
in the list, and returns the result as a string with 
the value rounded to three decimal places.
'''
'''
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
'''
'''
input: list of positive integers
output: all integers multiplied together, divided by the number of integers
- as string, rounded to 3 decimal places

Algorithm:

1. multiply all integers in list together
    - initialize variable multiplied = 1
    - for number in list:
    - multiplied *= number
2. divide multiplied by length of list
3. print as a formatted string
'''

def multiplicative_average(list):
    multiplied = 1

    for number in list:
        multiplied *= number
    
    result = multiplied / len(list)

    return f"{result:.3f}"

print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")