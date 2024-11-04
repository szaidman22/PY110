matrix = [
    [1, 5, 8, 5, 6, 7, 9],
    [4, 7, 2, 5, 6, 7, 9],
    [3, 9, 6, 5, 6, 7, 9],
    [5, 6, 7, 5, 6, 7, 9]
]

def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])

    outer_list = []
    for index_2 in range(n):
        inner_list = []
        for index_1 in range(m):
            inner_list.append(matrix[index_1][index_2])
        outer_list.append(inner_list)
    return outer_list

transpose(matrix)

new_matrix = transpose(matrix)

print(new_matrix)