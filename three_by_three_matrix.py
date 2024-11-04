matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

def transpose(matrix):
    list1 = []
    list2 = []
    list3 = []
    for list in matrix:
        list1.append(list[0])
        list2.append(list[1])
        list3.append(list[2])
    return([list1, list2, list3])


new_matrix = transpose(matrix)

print(new_matrix)
print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True