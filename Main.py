import GuessGame, MemoryGame, CurrencyRouletteGame, os, Score, Utils

def welcome(name):
    welcome = "Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    return welcome

def load_game():
    name = input("Please Enter your name: ")
    print(welcome(name))
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    while True:
     game = input("Please choose a game to play (1-3):")
     difficulty = input("Please choose difficulty (1-5):")
     if game not in ['1','2','3'] or difficulty not in ['1','2','3','4','5']:
         print("Invalid selection. Please try again")
         continue
     else:
        if game == '1':
            if MemoryGame.play(int(difficulty)):
                Score.add_score((int(difficulty) * 3) + 5)

        elif game == '2':
            if GuessGame.play(int(difficulty)):
                Score.add_score((int(difficulty) * 3) + 5)

        else:
            if CurrencyRouletteGame.play(int(difficulty)):
                Score.add_score((int(difficulty) * 3) + 5)

        response = input("Do you want to play again (y/n)?")
        if response == 'y':
            Utils.screen_cleaner()
            continue
        else:
            print("Goodbye")
            os.remove('scores.txt')

            break


load_game()



