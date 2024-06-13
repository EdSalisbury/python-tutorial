import json
import random

with open("trivia.json") as file:
    questions = json.load(file)

random.shuffle(questions)
num_questions = len(questions)
num_correct = 0

choices = ["A", "B", "C", "D"]

while len(questions):
    question = questions.pop()
    print(question.get("question", ""))
    choice_num = 0
    correct = ""
    for answer in question.get("answers", []):
        print(f"{choices[choice_num]}. {answer.get('option')}")
        if answer.get("correct"):
            correct = choices[choice_num]
        choice_num += 1

    guess = ""
    while not guess:
        guess = input("What is the answer: ")
        guess = guess.strip().upper()
        if guess not in choices:
            guess = ""

    if guess == correct:
        print("You are correct!")
        num_correct += 1
    else:
        print(f"Incorrect. The correct answer is {correct}.")
    
    print()

percent = round(num_correct / num_questions * 100)

print(f"Your score: {num_correct}/{num_questions} ({percent}%)")
