from time import sleep
import random
import sys

def generate_sequence(difficulty):
    RandomListOfIntegers = [random.randint(1, 101) for iter in range(difficulty)]
    return RandomListOfIntegers

def get_list_from_user(difficulty):
    numberList = []
    for i in range(0, difficulty):
        while True:
            number = input("\rEnter number: ")
            if not number.isdigit():
                print("Invalid input. Please try again")
                continue
            else:
                break
        numberList.append(int(number))

    return numberList


def is_list_equal(RandomListOfIntegers,numberList):
    if set(RandomListOfIntegers)  == set(numberList):
        print("Excellent!")
        return True
    else:
        print("Wrong guess")
        return False

def play(difficulty):
    RandomListOfIntegers = generate_sequence(difficulty)
    sys.stdout.write(str(RandomListOfIntegers)); sleep(0.7)
    numberList = get_list_from_user(difficulty)
    if is_list_equal(RandomListOfIntegers, numberList):
        return True
    else:
        return False


