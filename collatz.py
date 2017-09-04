def collatz(number):
     if number % 2 == 0:
        return(number // 2)
     else:
        return(number * 3 + 1)

        
try:
    userGuess = int(input('Enter a starting number: '))

    
    while userGuess != 1:
        userGuess = collatz(userGuess)
        print(userGuess)

    
except ValueError:
    print('You must enter a number')
