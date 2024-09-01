questions = (
    "In what country was the Caesar salad invented?",
    "What was the first fruit to be eaten on the Moon?",
    "In which Italian city was pizza first made?",
    "Which country has the most Michelin starred restaurants?"
)

options = (
    ("A. USA", "B. Italy", "C. Mexico"),
    ("A. Grape", "B. Peach", "C. Starfruit"),
    ("A. Naples", "B. Rome", "C. Palermo"),
    ("A. Spain", "B. France", "C. Austria"),
)

answers = ("C", "B", "A", "B")
guesses = []
score = 0
question_num = 0

print("----- QUIZ -----")

for question in questions:
    print(question)

    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print(f"Wrong, {answers[question_num]} is the correct answer")

    print("----- ----- -----")
    question_num += 1

print(f"Your score: {score}/{len(questions)} points")