import numpy as np

def GenNum():
    
    number = np.random.randint(101)
    print("There is given a number in range from 0 to 100.")
    print("You should try and guess what it is!")

    for answers in range(5):
        
        guess = int(input("Please insert your guess: \n"))
        
        if guess < 0 or guess > 100:
            print("Please try again. Given number out of range")
            
        if guess == number:
            print("Wow! You got it right! Amazing!")
            break
        elif guess < number:
            print("Oh no! Your number is too small")
            if answers == 0:
                if guess + 10 < number:
                    print("You should think a lot bigger!")
                elif guess + 10 > number:
                    print("You should think only a little bigger!")
            if answers == 1:
                if guess < number + 10:
                    print("Your number should be smaller than", number+10, "and bigger than", number-10)
                elif guess >= number + 10:
                    print("Your number should be smaller than", number+5, "and bigger than", number-5)
            if answers == 2:     
                if number%2 == 0:
                    print("The number you are looking for is even")
                else:
                    print("The number you are looking for is odd")
            if answers == 3:
                print("It's your last chance!")
        else:
            print("Oh no! Your number is too big") 
            if answers == 0:
                if guess - 10 > number:
                    print("Your number should be a lot smaller!")
                elif guess - 10 < number:
                    print("Your number should be only a little smaller!")
            if answers == 1:
                if guess < number + 10:
                    if number - 10 > 0:
                        print("Your number should be than", number+10, "and bigger than", number-10)
                    else:
                        print("Your number should be than", number+10, "and bigger than 0")
                
                elif guess >= number + 10:
                    if number - 5 > 0:
                        print("Your number should be than", number+5, "and bigger than", number-5)
                    else:
                        print("Your number should be than", number+5, "and bigger than 0")
            if answers == 2:     
                if number%2 == 0:
                    print("The number you are looking for is even")
                else:
                    print("The number you are looking for is odd")
            if answers == 3:
                print("It's your last chance!")
    else: 
        print()
        print("Sorry! You lost!")
        print("The answer was: " + str(number))

GenNum()
