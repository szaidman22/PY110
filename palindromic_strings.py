'''
Write a function that returns True if the string passed as an argument 
is a palindrome, False otherwise. A palindrome reads the same forwards 
and backwards. For this problem, the case matters and all characters matter.

P
- input: string
- output: boolean
- explicit rules: palindrome is the same string read forwards or backwards
    - case and all characters matter
- implicit rules: if string length 0, the should be an error handled
    - if string length 1, I guess it's a palindrome
E

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

D
- string input

A

- GET string input
- IF the length of the string is less than 1, print a string saying to enter another string
- TEST if the input string reversed is equal to the input string, return True, otherwise return False

'''

#Part 1
'''
def palindrome(string):
    if len(string) >= 1:
        return string == string[::-1]
    print("Palindrome requires a string of at least one character in length.")

print(palindrome("barab"))
'''
#Part 2
def is_real_palindrome(string):
    stripped_string = ''.join([c.casefold() for c in string if c.isalnum()])

    if len(stripped_string) >= 1:
        return stripped_string == stripped_string[::-1]
    print("Palindrome requires a string of at least one alpha-numeric character in length.")

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True