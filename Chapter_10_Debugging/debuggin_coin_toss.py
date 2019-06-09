#! python3

'''
The following program (buggy_code()) is meant to be a simple coin toss guessing game.
The player gets two guesses (it’s an easy game). However, the program has several bugs in it.
Run through the program a few times to find the bugs that keep the program from working correctly.
'''

import random, logging


def buggy_code():
    guess = ""
    while guess not in ("heads", "tails"):
        print("Guess the coin toss! Enter 'heads' or 'tails':")
        guess = input()
    toss = random.randint(0,1)  # 0 is tails, 1 is heads
    if toss == guess:
        print("You got it")
    else:
        print("Nope! Guess again!")
        guesss = input()
        if toss == guess:
            print('You got it')
        else:
            print("The guess is incorrect. You might have missed the point of the game...")


def debugging_code():
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    guess = ""

    while guess not in ("heads", "tails"):
        print("Guess the coin toss! Enter 'heads' or 'tails':")
        guess = input()
        logging.debug(f"User guess is {guess}")
    toss = random.randint(0,1)
    logging.debug(f"Random value is {toss}")
    logging.debug(f"{guess} == {toss}?")  # detects 1st bug

    if toss == guess:
        print("You got it")
    else:
        print("Nope! Guess again!")
        guesss = input()
        logging.debug(f"User guess is {guesss}")
        logging.debug(f"{guess} == {toss}?")  # detects 2nd bug
        if toss == guess:
            print('You got it')
        else:
            print("The guess is incorrect. You might have missed the point of the game...")


def fixed_code():
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.disable(logging.CRITICAL)
    guess = ""

    while guess not in ("heads", "tails"):
        print("Guess the coin toss! Enter 'heads' or 'tails':")
        guess = input()
        logging.debug(f"User guess is {guess}")
    toss = random.randint(0,1)  # fixed 1st bug

    if toss == 0:
        toss = "tails"
    else:
        toss = "heads"
    logging.debug(f"Random value is {toss}")
    logging.debug(f"{guess} == {toss}?")

    if toss == guess:
        print("You got it")
    else:
        print("Nope! Guess again!")
        guess = input()  # fixed 2nd bug
        logging.debug(f"User guess is {guess}")
        logging.debug(f"{guess} == {toss}?")
        if toss == guess:
            print('You got it')
        else:
            print("The guess is incorrect. You might have missed the point of the game...")


# buggy_code()
# debugging_code()
fixed_code()