'''
Write a function that combines two lists passed 
as arguments and returns a new list that contains 
all elements from both list arguments, with each 
element taken in alternation.

You may assume that both input lists are non-empty, 
and that they have the same number of elements.
'''
'''
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
'''
'''
input: two lists
output: one list alternating one element from list 1, one from list two 
in order so on
rules: lists are not empty and have the same number of elements

Algorithm:

1. get length of lists
1.5 initialize new empty list
2. for index in range(length)
 - extend list with input list elements at that index
3. return new list
'''

def interweave(list1, list2):
    length = len(list1)
    new_list = []
    for index in range(length):
        new_list.extend([list1[index], list2[index]])
    
    return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interweave(list1, list2) == expected)      # True