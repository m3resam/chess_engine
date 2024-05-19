# This program asks for a string and searches the vowels in that string
# asks user an input string, set vowel counter to 0 and initialize empty list
word = input()
vowel = 0
V = []

# loop through each char of word, if char is equal to a vowel +1 to counter and append vowel to list
for j in word:
    if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
        vowel += 1
        V.append(j)

# print results
# if we want to print a mix between string and int/float whe can use print(f'string {int/float}') to write faster
print(f'The vowels in "{word}" are: ' + str(V)) 
print(f'There are {vowel} vowels in total')
