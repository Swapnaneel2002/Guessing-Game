import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    lower_limit = 1
    upper_limit = 100
    number_to_guess = random.randint(lower_limit, upper_limit)
    attempts = 0
    play_again = True

    while play_again:
        attempts = 0
        print(f"\nI have chosen a number between {lower_limit} and {upper_limit}. Can you guess it?")
        
        while True:
            try:
                user_guess = int(input("Enter your guess: "))
                attempts += 1

                if user_guess < number_to_guess:
                    print("Too low!")
                elif user_guess > number_to_guess:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")

        play_again_input = input("\nDo you want to play again? (y/n): ").lower()
        if play_again_input != 'y':
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
