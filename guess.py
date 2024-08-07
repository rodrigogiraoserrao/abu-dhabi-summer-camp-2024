from random import randint

# The computer picks a random secret number.
secret_number = randint(1, 100)

# We prepare the variable for the game to run.
guess = 0
while guess != secret_number:
    # Ask the user for their guess:
    guess = int(input("Type your guess: "))
    # Give feedback to the user:
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You win!")
