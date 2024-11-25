'''
input: list of values
output: list of values, sorted, inplace (mutate the list)
algorithm:
1. get input list
2. 

'''

def bubble_sort(list):
    indexes = range(len(list) - 1)

    def swaperoo():
        swap_count = 0
        for x in indexes:
            first = list[x]
            second = list[x + 1]
            if first > second:
                swap_count += 1
                list[x] = second
                list[x + 1] = first
        return swap_count

    while swaperoo() > 0:
        swaperoo()
            
        
squee = [4,5,7,2,4,5,1]
print(squee)
bubble_sort(squee)
print(squee)

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True



# x = 1

# while True:
#     x += 1
#     print(x)
#     if x > 8:
#         break