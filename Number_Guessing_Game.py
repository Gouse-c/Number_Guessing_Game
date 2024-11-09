import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
