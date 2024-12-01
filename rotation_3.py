'''
Take the number 735291 and rotate it by one digit to the left, 
getting 352917. Next, keep the first digit fixed in place and 
rotate the remaining digits to get 329175. Keep the first two 
digits fixed in place and rotate again to get 321759. Keep the 
first three digits fixed in place and rotate again to get 321597. 
Finally, keep the first four digits fixed in place and rotate the 
final two digits to get 321579. The resulting number is called the 
maximum rotation of the original number.

Write a function that takes an integer as an argument and returns 
the maximum rotation of that integer. You can (and probably should) 
use the rotate_rightmost_digits function from the previous exercise.
'''
'''
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
'''
'''
algorithm:
basically, we are taking the input number, rotating by 1,
   ignoring the previous digit(s) and rotating by one again
   until the end of the number.

using the rightmost digits function as a starting point,
we would want to eliminate the digits input and instead 
have a for loop that has the "digits" go from the length
of the number of digits down to 1.

1. 
'''

def max_rotation(integer):
    int_string = str(integer)
    num_len = len(int_string)

    if num_len == 1:
        return integer

    for digit in range(num_len,1,-1):
        stop_index = num_len - digit
        result = int_string[:stop_index] + int_string[stop_index + 1:] + int_string[stop_index]
        int_string = result
    
    return int(result)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True