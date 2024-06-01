def collatz(number):
    if number % 2 == 0:
        result = number // 2  
    elif number % 2 == 1:
        result = 3 * number + 1
    print(result)
    return result

while True:
    try:
        user_input = int(input('Type an integer: '))
        if user_input <= 0:
            print('Please enter a positive integer.')
            continue
        break
       
    except ValueError:
        print('Error:Use only integers!')
        continue

 while user_input != 1:
            user_input = collatz(user_input)
        break
    
    



    
    
    


        
