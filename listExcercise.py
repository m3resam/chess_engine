from random import *

# Create a list
n = []

'''
print('Enter a positive int: ')
N = int(input())
while N > 0:
    print('Enter int: ')
    m = int(input())
    n.append(m)
    N -= 1
'''

# Loop 10 times and append a random number between 1 and 100
for i in range(10):
    m = randint(1,100)
    n.append(m)
    
# Look for the highest numer in the list and it's position
max = n[0]
pos = 0
for i in n:
    pos += 1
    if i > max:
        max = i
        posd = pos

# Print results
print(n)
print(max)
print(posd)
    
    
    
