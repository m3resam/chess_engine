
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        userInput = int(input('Type an integer: '))
        userInput = collatz(userInput)
        while userInput != 1:
            userInput = collatz(userInput)
        break
    
    except ValueError:
        print('Error:Use only integers!')
        continue
    
    



    
    
    


        
