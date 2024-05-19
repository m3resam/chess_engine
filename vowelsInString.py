word = input()
vowel = 0
V = []

for j in word:
    if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
        vowel += 1
        V.append(j)

print(f'The vowels in "{word}" are: ' + str(V)) 
print(f'There are {vowel} vowels in total')
