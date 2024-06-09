def swap(x, y, z):

    if x > y:
        x, y, z = y, x, z
        #print(x,y,z)

    if z < x:
        x, y, z = z, y, x
        #print(x,y,z)
        x, y, z = x, z, y
        #print(x,y,z)

    elif z < y:
        x, y, z = x, z, y
        #print(x,y,z)
        
    return x, y, z

def main():
    print('In this program you need to enter 3 integers a, b and c')
    print('Enter a: ')
    a = int(input())
    print('Enter b: ')
    b = int(input())
    print('Enter c: ')
    c = int(input())
    
    print(swap(a,b,c))

main()



