from forex_python.converter import CurrencyRates
import random

def get_money_interval(difficulty):
    rate = CurrencyRates().get_rate('USD', 'ILS')
    interval = []
    generated_number = random.randint(1, 100)
    for i in range(0, 6 - difficulty):
        interval.append(round((rate * generated_number) + i - (difficulty/2)))

    return generated_number, interval


def get_guess_from_user(generated_number):
    while True:
        guess_number = input("Pleasse guess the currency in ILS for " + str(generated_number) + " USD: ")
        if not guess_number.isdigit():
            print("Invalid input. Please try again")
            continue
        else:
            break

    return int(guess_number)

def play(difficulty):

    generated_number, list = get_money_interval(difficulty)
    guess_number = get_guess_from_user(generated_number)

    if guess_number in list:
        print("Currecny is in interval. Well done")
        return True
    else:
        print("Currecny is not in interval.")
        return False


