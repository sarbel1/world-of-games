import random

def generate_number(difficulty):
   generated_number = random.randint(1, difficulty)
   return generated_number

def get_guess_from_user():
    while True:
        guess = input("Please guess a number: ")
        if not guess.isdigit():
            print("Invalid input. Please try again")
            continue
        else:
            break

    return int(guess)

def compare_results(generated_number,guess):
    if generated_number  == guess:
        print("Excellent!")
        return True
    else:
        print("Wrong guess")
        return False


def play(difficulty):
    generated_number = generate_number(difficulty)
    guess = get_guess_from_user()
    if compare_results(generated_number, guess):
        return True
    else:
        return False


