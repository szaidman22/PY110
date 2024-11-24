'''
Write a function that takes a list of numbers 
and returns a list with the same number of elements, 
but with each element's value being the running total 
from the original list.

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True


P
- input: list of numbers
- output: new list with numbers as running total
- implicit rules: can be 0, negative or positive, empty list or one number
E
- see examples
D
- lists
A
- list of numbers as input
- create a variable to store the running total
- set the default value to 0
- For each number in the list
    - add that number to the running total
    - save that value to a new list
C
'''

def running_total(list):
    running = 0
    output = []
    for number in list:
        running += number
        output.append(running)
        
    
    return output



print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True