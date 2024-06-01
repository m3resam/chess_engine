# This function takes one parameter
def collatz(number):
    # Checks if it's even
    if number % 2 == 0:
        # Prints result
        print(number // 2)
        # Returns printed value
        return number // 2
    # Checks if it's odd
    elif number % 2 == 1:
        # Prints result
        print(3 * number + 1)
        # Returns printed value
        return 3 * number + 1

# Loops and checks if user input is compatible with program
while True:
    # If the input is an integer try to run the Collatz sequence
    try:
        userInput = int(input('Type an integer: '))
        userInput = collatz(userInput)
        while userInput != 1:
            userInput = collatz(userInput)
        break

    # If the input is not an integer handle error exception and rerun the program
    except ValueError:
        print('Error:Use only integers!')
        continue
    
    



    
    
    


        
