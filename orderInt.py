

    
'''
if a > b:
    k = a
    a = b
    b = k

if c < a:
    k = a
    a = c
    c = k
    k = b
    b = c
    c = k

elif c < b:
    k = b
    b = c
    c = k
'''

def swap(x, y):
    x, y = y, x
    return

def main():
    print('In this program you need to enter 3 integers a, b and c')
    print('Enter a: ')
    a = int(input())
    print('Enter b: ')
    b = int(input())
    print('Enter c: ')
    c = int(input())
    
    if a > b:
        swap(a,b)

    if c < a:
        swap(a, c)
        swap(b, c)
        
    elif c < b:
        swap(b, c)

    print(a, b, c)


main()




