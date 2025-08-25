# import argparse
#
# parser = argparse.ArgumentParser(description="Greet the user")
# parser.add_argument("-n", "--name", metavar="name",
#                     required=True, help="Pass name of the user to be greeted")
# args = parser.parse_args()
# result = f"Hello {args.name}!"
# print(result)

# create a list of Q and A. User plays and get a score


def QA():
    print("Questions")
    questions = [{
        "questions": "1. Who was the first President of the United States?\nA. John Roosevelt \nB. John. F Kennedy \nC. George Washington \nD. George Bush",
        "answer": "C"},

        {"questions": "2. In which year did World War II end?\nA. 1914 \nB. 1945 \nC. 1928\nD. 1943",
         "answer": "B"},

        {
            "questions": "3. Which ancient civilization built the Great Pyramids of Giza?\nA. Mongolians \nB. Egyptians \nC. Persians \nD. Sudanese",
            "answer": "B"},

        {
            "questions": "4. Who wrote the Declaration of Independence for the United States?\nA. John Roosevelt \nB. Thomas Jefferson \nC. George Washington \nD. Kelton Reeds",
            "answer": "B"},

        {
            "questions": "5. What was the name of the ship that carried the Pilgrims to America in 1620?\nA. Titanic \nB. Lander \nC. Black Pearl \nD. The Mayflower",
            "answer": "D"},

        {
            "questions": "6. Which empire was ruled by Julius Caesar?\nA. Persians \nB. Macedonians \nC. Romans \nD.Egyptians",
            "answer": "C"},

        {
            "questions": "7. What event marked the beginning of the French Revolution?\nA. WWI \nB. The great famine \nC. Storming of the Bastille\nD. Slave trade",
            "answer": "C"},

        {
            "questions": "8. Who was the first woman to win a Nobel Prize?\nA. Marie curie \nB. Annie mccurley\nC. Marry slessor \nD. Magaret Thatcher",
            "answer": "A"},

        {
            "questions": "9. Which war was fought between the North and South regions of the United States?\nA. Declaration war \nB. Independence war \nC. War of the Amaegedon \nD. The American Civil War",
            "answer": "D"},

        {
            "questions": "10. What was the Berlin Wall a symbol of during the Cold War?\nA. WW2 \nB. Wall of Jerusalem \nC. Royal protests \nD.  division between Communist and Democratic Germany",
            "answer": "D"}, ]

    score = 0
    for every_variable in questions:
        while True:
            print(every_variable["questions"])
            user_answer = input(f"\nEnter your answer:\n").strip().lower()
            if user_answer in ["a", "b", "c", "d".strip().lower()]:
                if user_answer.lower() == every_variable["answer"].strip().lower():
                    print("Correct answer!🎉")
                    score += 1
                    print(f"{score}/{len(questions)}\n\n")

                else:
                    print(f"Wrong answer😒\n The correct answer is {every_variable["answer"]}")
                    print(f"{score} /{len(questions)}\n\n")
                break
            else:
                print("Please, choose either A,B,C or D!\n")

    if score >= 5:
        print("Not bad! 😉")
    else:
        print("Tough luck, try again?")

    print(f"Your total score is {score}/{len(questions)}\n")


QA()
