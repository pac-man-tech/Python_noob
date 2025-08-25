import time
import random
import argparse
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


print("Welcome to the History quiz!🥳\n")


def qa(name="Playerone"):
    print(f"Hafa, {name}😊\nAre you ready?")
    time.sleep(1)
    print("\nLet's begin!")

    questions = [{
        "questions": "Q. Who was the first President of the United States?\nA. John Roosevelt \nB. John. F Kennedy \nC. George Washington \nD. George Bush",
        "answer": "C"},

        {"questions": "Q. In which year did World War II end?\nA. 1914 \nB. 1945 \nC. 1928\nD. 1943",
         "answer": "B"},

        {
            "questions": "Q. Which ancient civilization built the Great Pyramids of Giza?\nA. Mongolians \nB. Egyptians \nC. Persians \nD. Sudanese",
            "answer": "B"},

        {
            "questions": "Q. Who wrote the Declaration of Independence for the United States?\nA. John Roosevelt \nB. Thomas Jefferson \nC. George Washington \nD. Kelton Reeds",
            "answer": "B"},

        {
            "questions": "Q. What was the name of the ship that carried the Pilgrims to America in 1620?\nA. Titanic \nB. Lander \nC. Black Pearl \nD. The Mayflower",
            "answer": "D"},

        {
            "questions": "Q. Which empire was ruled by Julius Caesar?\nA. Persians \nB. Macedonians \nC. Romans \nD. Egyptians",
            "answer": "C"},

        {
            "questions": "Q. What event marked the beginning of the French Revolution?\nA. WWI \nB. The great famine \nC. Storming of the Bastille\nD. Slave trade",
            "answer": "C"},

        {
            "questions": "Q. Who was the first woman to win a Nobel Prize?\nA. Marie curie \nB. Annie mccurley\nC. Marry slessor \nD. Magaret Thatcher",
            "answer": "A"},

        {
            "questions": "Q. Which war was fought between the North and South regions of the United States?\nA. Declaration war \nB. Independence war \nC. War of the Amaegedon \nD. The American Civil War",
            "answer": "D"},

        {
            "questions": "Q. What was the Berlin Wall a symbol of during the Cold War?\nA. WW2 \nB. Wall of Jerusalem \nC. Royal protests \nD. division between Communist and Democratic Germany",
            "answer": "D"}, ]
    score = 0
    random.shuffle(questions)
    real = random.sample(questions, 10)
    for every_variable in random.sample(questions, 10):
        print(every_variable["questions"])

        def calc_questions(ever_variable):
            attempt = 0
            nonlocal score
            while attempt < 2:
                user_answer = input(f"\n {name}, Please enter your answer:\n").strip().lower()
                if user_answer in ["a", "b", "c", "d"]:
                    if user_answer.lower() == every_variable["answer"].strip().lower():
                        print(f"Correct answer, {name}!🎉")
                        score += 1
                        print(f"{score}/{len(questions)}\n\n")
                        return

                    else:
                        attempt += 1
                        if attempt < 2:
                            print(f"{name},you have one more attempt")
                        else:
                            print(f"Wrong answer again!😒\n The correct answer is {every_variable["answer"]}")
                            print(f"{score} /{len(real)}\n\n")  # i want to divide by samples, not working tho
                else:
                    print("Please, choose either A,B,C or D!\n")

        calc_questions(every_variable)
        time.sleep(0.7)

    if score >= 5:
        print("Not bad! 😉")
    else:
        print(f"{name},not good enough. You should try again!")

    print(f"Your total score is {score}/{len(real)}\n")

    def play_again():
        while True:
            again = input(f"{name},do you want to play again?\ny for Yes\nn for No\n")
            if again == ("y".strip().lower()):
                clear()
                print("\nWelcome back to the game!")
                qa()
                break
            elif again == ("n".strip().lower()):
                clear()
                print(f"Thanks for playing, {name}!")
                break
            else:
                print(f"{name}, please enter a valid input!")

    play_again()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quiz test")
    parser.add_argument("-n", "--name", metavar="name",
                        required=True, help="input name of gamer")
    args = parser.parse_args()

    quizz = qa(args.name)
    quizz
