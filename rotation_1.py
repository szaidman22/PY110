'''
Write a function that rotates a list by moving the first 
element to the end of the list. Do not modify the original 
list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
'''

'''
# All of these examples should print True
print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
'''

'''
input: list
output: new list, with first element of old list in last position
rules: do not mutate inputlist

Algorithm:
1. save a slice of input list from second element to end as new list
2. append the first element of the input list to the new list and return
'''

def rotate_list(input_list):
    if not isinstance(input_list, list):
        return None
    elif len(input_list) == 0:
        return input_list
    else:
        rotated = input_list[1:]
        rotated.append(input_list[0])
        return rotated
    
print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])