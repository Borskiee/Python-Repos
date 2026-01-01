# Simple Quiz Game

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which number is even?",
        "options": ["A. 3", "B. 7", "C. 12", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which is a programming language?",
        "options": ["A. Python", "B. Snake", "C. Cobra", "D. Lion"],
        "answer": "A"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").upper()
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")

print(f"\nYour final score: {score}/{len(questions)}")
