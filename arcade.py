from Rps import rps
from guess_number import guess
import sys
import argparse
import time
import os
from scramble import scramble
from history_quiz import qa


def clear():
    os.system("cls" if os.name == "nt"
              else "clear")


def lobby(name="gamer"):
    time.sleep(0.6)
    clear()
    print(f"\nHello {name}, Welcome to the Arcade!")
    welcome_back = False
    while True:
        if welcome_back:
            print(f"{name}, welcome back to the Arcade\n\n")
        user_input = input(
            f'{name}, please enter your game choice:\n1 = Guess the number\n2 = Rock-paper-scissors\n3 = Word Scramble\n4 = History quizz\n\n\n   press "x" to quit the Arcade\n\n')
        if user_input.strip().lower() == "x":
            print(f"Thanks for playing {name}, see you soon!")
            sys.exit()
        welcome_back = True
        if user_input == "1":
            guess(name)()
        elif user_input == "2":
            rps(name)()
        elif user_input == "3":
            scramble(name)
        elif user_input == "4":
            qa()()
        else:
            print(f"{name}, please enter a valid input of 1 ,2 or x")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Name of player")
    parser.add_argument("-n", "--name", metavar="name", required=True, help="Enter name of gamer in the Arcade")
    args = parser.parse_args()
    final = f" are you ready{args.name}?"

    lobby(args.name)
