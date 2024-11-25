'''
Modify the word_sizes function from the previous 
exercise to exclude non-letters when determining 
word size. For instance, the word size of "it's" is 3, not 4.

'''
'''
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
'''

'''
P:
- input: string
- ouptut: dictionary with keys length of word and value count of words of that length
- explicit: string has words space-separated
- implicit: only letters count

Algorithm:

1. GET input string
2. split input string (by space) into list of words
3. create empty dictionary
4. for each word in the list:
    - remove non-alphabetic characters using list comprehension and join method
    - get the length of the word
    - if not in the dictionary, add to the dictionary as a key with value 1
    - if in the dictionary, increase that key's value by 1
5. return the dicitonary
'''


def word_sizes(string):
    word_list = string.split()
    sizes = {}

    for word in word_list:
        only_alpha = ''.join([char for char in word if char.isalpha()])
        length = len(only_alpha)
        if length not in sizes:
            sizes[length] = 1
        else:
            sizes[length] += 1
    
    return sizes

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})