'''
Given a string of words separated by spaces, 
write a function that swaps the first and last 
letters of every word.

You may assume that every word contains at 
least one letter, and that the string will always 
contain at least one word. You may also assume that 
each string contains nothing but words and spaces, 
and that there are no leading, trailing, or repeated spaces.
'''
'''
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
'''
'''
P:
- input: string of words separated by spaces
- output: string with first and last character of each word swapped
- explicit: all words have at least one letter, string only has words and spaces,
no leading or trailing or repeated spaces
- implicit: keep case

Algorithm:

1. GET string of words
2. create list of words in string by splitting string by spaces
3. create empty list for new words
3. for each word in the list of words:
    - create a list of characters in the word by converting word to list
    - swap the first and last indexed character in the list
    - rejoin the characters in the list to create the new word
    - append the new word to the list of new words
4. join the list of new words with a space and return it
'''

def swap(string):
    word_list = string.split()
    new_word_list = []

    for word in word_list:
        chars = list(word)
        first = chars[0]
        last = chars[-1]
        chars[0] = last
        chars[-1] = first
        new_word = ''.join(chars)
        new_word_list.append(new_word)
    
    new_string = ' '.join(new_word_list)
    return new_string


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True