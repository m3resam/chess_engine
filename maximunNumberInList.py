from random import *

L = []

for i in range(10):
    n = randint(1,100)
    L.append(n)

max = L[0]

for i in L:

    if i > max:
        max = i

print(L)
print(max)
