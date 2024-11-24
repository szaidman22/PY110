'''
P
- input: 6 numbers (assume integers)
- output: string, "[6th] number is [not] in [list of first 5 numbers]"
- explicit rules: must have 6 number inputs
- implicit rules: can be negative, assuming they should be integers

E
- see above

D
- will need a list for the input numbers

A
- GET user input, 6 separate numbers one after another
    - CONVERT string input to integer
    - INSERT first 5 integers into a list
- for 6th input string converted into an integer
- test if it is a member of the list (boolean)
- print results of test accordingly
    - if True, print __ is in [list]
    - else, print __ isn't in [list]
'''




num_list = [input("Enter the first number: "), 
            input("Enter the second number: "),
            input("Enter the third number: "),
            input("Enter the fourth number: "),
            input("Enter the fifth number: ")]

last_num = input("Ener the last number: ")

if last_num in num_list:
    print(f"{last_num} is in {','.join(num_list)}")
else:
    print(f"{last_num} isn't in {','.join(num_list)}")
