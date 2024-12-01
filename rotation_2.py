'''
Write a function that rotates the last count digits 
of a number. To perform the rotation, move the first 
of the digits that you want to rotate to the end and 
shift the remaining digits to the left.
'''
'''
print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
'''
'''
input: integer, count of digits
output: rotated number as described above
rules: integer as input, count is within thenumber of digits of the integer

algorithm:
1. convert integer input to string
2. get the count of digits input, subtract from length of string (stop index)
3. slice string up to stop index 
4. slice string from stop index + 1 to end
5. return step 3 + step 4 + string[stop index] (converted back to integer)
'''

def rotate_rightmost_digits(integer, digits):
    int_string = str(integer)
    num_len = len(int_string)
    stop_index = num_len - digits

    return int(int_string[:stop_index] + int_string[stop_index + 1:] + int_string[stop_index])

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True