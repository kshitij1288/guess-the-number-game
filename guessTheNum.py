
import random


print("Welcome to number guessing game!")

guesses = 0
number = random.randint(0, 10)


while( guesses < 3 ):
    u_guess = int(input("Have a guess: "))

    if u_guess == number:
        print("Well done, you win!")
        break
    elif u_guess > number:
        print("Your guess was too high.")
        guesses = guesses + 1
    elif u_guess < number:
        print("Your guess was too low.")
        guesses = guesses + 1
    else:
        print("There was an error.")

if guesses == 5:
    print("You lose!")
    print("The number was: " + str(number))
