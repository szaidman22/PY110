list1 = [3, 5, 7]
list2 = [9, 10, 11]

def multiply_list(l1, l2):

    new_list = []

    for index in range(0, len(l1)):
        new_list.append(l1[index] * l2[index])
    
    return new_list

print(multiply_list(list1, list2) == [27, 50, 77])  # True