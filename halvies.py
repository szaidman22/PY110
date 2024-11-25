'''
Write a function that takes a list as an 
argument and returns a list that contains 
two elements, both of which are lists. Put the 
first half of the original list elements in the 
first element of the return value and put the 
second half in the second element. If the original 
ist contains an odd number of elements, place the 
middle element in the first half list.
'''

'''
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
'''
'''
P:
input: list
output: list of two lists, with original list elements split in half by index
explicit rules: if list has odd number of elements, add middle element to first half
implicit rules: if list has one element, it should go in the first half and second list should be empty
- if list is empty, both output lists should be empty

Algorithm:
1. GET input list
2. get length of input list
    - if even: divide by two
    - if odd: divide by two and round up
    - subtract one, save this as the index cutoff for the first half
3. create empty lists for first and second half
4. for item, index in input list
    - if index is <= cutoff, add to the first half
    - if index is > cutoff, add to the second half
    - if list is empty, break
return [first half, second half]
'''

def halvsies(list):
    if len(list) == 0:
        return [[], []]
    elif len(list) % 2 == 0:
        cutoff = (len(list) / 2) - 1
    elif len(list) % 2 > 0:
        cutoff = (len(list) / 2)

    first = []
    second = []

    for index, item in enumerate(list):
        if index <= cutoff:
            first.append(item)
        else:
            second.append(item)
    
    return [first, second]

#ANSWER
def halvsies(lst):
    half = (len(lst) + 1) // 2
    print(half)
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]

print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

