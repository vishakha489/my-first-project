import random
def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Optional: Limit guesses for added challenge
    
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                return  # End the game
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")
# Run the game
if __name__ == "__main__":
    guess_the_number()