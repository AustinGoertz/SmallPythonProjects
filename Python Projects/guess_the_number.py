import random

def generate_answer(num_min: int, num_max: int) -> int:
    return random.randint(num_min, num_max)

def get_user_guess(num_min: int, num_max: int):
    user_guess: str = input("Enter your guess: ")
    print()
    
    while ((not user_guess.isdigit()) or int(user_guess) < num_min or int(user_guess) > num_max):
        print("Invalid guess, enter a number between 1 and 100: ")
        print()
        user_guess: str = input("Enter your guess: ")

    return int(user_guess)

def validate_guess(guess: int, answer: int) -> bool:
    if (guess < answer):
        print("The number we are looking for is bigger than your guess, try again.")
        print()
        return False
    elif (guess > answer):
        print("The number we are looking for is smaller than your guess, try again.")
        print()
        return False
    else:
        print("Correct, well done!")
        return True


def main():

    num_min: int = 1
    num_max: int = 100
    answer: int = generate_answer(num_min, num_max)
    print(f'Welcome to guess the number! Guess the random number between {num_min} and {num_max}.')

    
    guess: int = get_user_guess(num_min, num_max)
    num_guesses = 1

    while(not validate_guess(guess, answer)):
        guess = get_user_guess(num_min, num_max)
        num_guesses += 1
    
    print(f'It took you {num_guesses} guesses to win the game!')

if __name__ == '__main__':
    main()