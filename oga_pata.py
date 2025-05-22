# build a rock paper scissor game

import sys
import random
from enum import Enum
import argparse
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def oga(name):
    game_count = 0
    player_count = 0
    computer_count = 0

    def game():
        nonlocal name
        nonlocal player_count
        nonlocal computer_count

        class RPS(Enum):
            Rock = 1
            Paper = 2
            Scissor = 3

        player = input(
            f"\nPlease enter... \n1 for Rock  \n2 for Paper\n3 for Scissor\n\n")  # when too long alt+z wraps  it to the next line
        if player not in ["1", "2", "3"]:
            print("Please enter 1, 2 or 3:")
            return game()
        gameplay = int(player)

        computer = random.randint(1, 3)

        print(f"\nYou chose  {str(RPS(gameplay)).replace('RPS.', "")}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', "")}.\n")

        def nests(gameplay, computer_play):
            nonlocal player_count
            nonlocal computer_count
            if gameplay == 1 and computer_play == 3:
                player_count += 1
                return f"🥳{name} wins!"
            elif gameplay == 2 and computer_play == 1:
                player_count += 1
                return f"🥳{name} wins!"
            elif gameplay == 3 and computer_play == 2:
                player_count += 1
                return f"🥳{name} wins!"
            elif gameplay == computer_play:
                return "😲Game tie!"
            else:
                computer_count += 1
                return f"sorry {name},🐍Python won this round"

        nest_play = nests(gameplay, computer)
        print(nest_play)
        nonlocal game_count
        game_count += 1
        print(f"\nGame count is {game_count}")
        print(f"{name}'s count is {player_count}")
        print(f"Python count is {computer_count}")
        while True:
            kp = input(f"\nWill you keep playing, {name}?\n Enter Y for yes\n Enter Q to quit\n")
            if kp.lower() == "y":
                return oga_pata()
            else:
                print(f"🎉🎉🎉\nThanks for playing, {name}!")
                clear()
                if __name__ == "__main__":
                    sys.exit(f"Goodbye {name}😊👋")
                else:
                    return

    return game


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provide personalized gaming experience")
    parser.add_argument("-n", "--name", metavar="name of gamer",
                        help="provide name of gamer", required=True)
    args = parser.parse_args()

    oga_pata = oga(args.name)
    oga_pata()
