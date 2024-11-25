'''
Write a function that takes a string consisting of 
zero or more space-separated words and returns a dictionary
that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

'''
'''
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
'''

'''
P:
- input: string
- ouptut: dictionary with keys length of word and value count of words of that length
- explicit: string has words space-separated
- implicit: any character counts, including punctuation

Algorithm:

1. GET input string
2. split input string (by space) into list of words
3. create empty dictionary
4. for each word in the list:
    - get the length of the word
    - if not in the dictionary, add to the dictionary as a key with value 1
    - if in the dictionary, increase that key's value by 1
5. return the dicitonary
'''


def word_sizes(string):
    word_list = string.split()
    sizes = {}

    for word in word_list:
        length = len(word)
        if length not in sizes:
            sizes[length] = 1
        else:
            sizes[length] += 1
    
    return sizes

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})