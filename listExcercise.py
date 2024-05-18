from random import *

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

for i in range(10):
    m = randint(1,100)
    n.append(m)
    

max = n[0]
pos = 0
for i in n:
    pos += 1
    if i > max:
        max = i
        posd = pos

print(n)
print(max)
print(posd)
    
    
    
