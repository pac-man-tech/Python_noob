import random
import sys
import argparse
import time
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def guess(name="Gamer"):
    score = 0
    attempt = 0
    print(f"{name},welcome to Guess my number!\n")
    print("are you readddyy?....")

    time.sleep(0.7)

    def guess_num():
        nonlocal score
        nonlocal attempt
        while attempt < 10:
            python_input = random.choice("123")
            user_input = input(str(f"Please input your guess, {name}:\n"))
            python_guess = (int(python_input))
            if user_input in ("1", "2", "3"):
                user_guess = (int(user_input))
                if user_guess == python_guess:
                    print(f"{name},na odogwu you be o! oya nau🤜🤛\n")
                    attempt += 1
                    score += 1
                    total = (score / attempt) * 100
                    print(f"Your score is {total}%")
                else:
                    print(f"Wrong!,python's guess was {python_guess}")
                    attempt += 1
                    total = (score / attempt) * 100
                    print(f"{name},your score is {total}%")
            else:
                print(f"{name},please enter any number between 1, 2 and 3")
        else:
            print(f"{name}, you have played 10 times!\n")
            total = (score / attempt) * 100
            print(f"Your final score is {total}%, welldone {name}!")

        while True:
            again = input(f"\nGGs {name}, do you want to play again?\nEnter y for yes\nEnter n for no\n")
            if again == ("y").strip().lower():
                return guess(name)()
            else:
                print(f"{name}, Thanks for playing")
                clear()
                if __name__ == "__main__":
                    sys.exit(f"{name}, goodbye!😊👋")
                else:
                    return

    return guess_num


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="guess the number in python's mind")
    parser.add_argument("-n", "--name", metavar="name", required=True, help="Input name value for the game")
    args = parser.parse_args()
    result = f"Hello, {args.name}!"
    print(result)

    game_time = guess(args.name)
    game_time()
