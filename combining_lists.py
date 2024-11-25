'''
Write a function that takes two lists as 
arguments and returns a set that contains 
the union of the values from the two lists. 
You may assume that both arguments will always be lists.
'''
'''
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
'''
'''
P:
input: two lists
output: set with union of the values from the two lists
rules: lists only have numbers, lists can only have hashable values

Algorithm:
1. create a list that is list 2 appended to list 1
2. convert to a set
3. return the set
'''

def union(list1, list2):
    return set(list1 + list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True