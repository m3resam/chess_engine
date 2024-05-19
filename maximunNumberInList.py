# This program creates a list with 10 random numbers and searches the highest number in the list
# import random module
from random import *

# initialize an empty list
L = []

# append 10 random numbers from 1 to 100 to the list
for i in range(10):
    n = randint(1,100)
    L.append(n)

# declare the first value in the list as the maximum number
max = L[0]

# loop through the list, if next number is greater than previuos, set next number as max and so on till end of list
for i in L:
    if i > max:
        max = i

# print results
print(L)
print(max)
