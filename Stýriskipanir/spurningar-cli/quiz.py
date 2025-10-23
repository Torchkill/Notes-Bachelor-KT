import os
import re
import json
from datetime import datetime

# set working dirs
cwd = os.getcwd() + os.sep
inputDir = os.path.join(cwd, "questions")
outputDir = os.path.join(cwd, "results")
os.makedirs(outputDir, exist_ok=True)  # ensure results dir exists


def natural_key(s):
    """Turn 'Cap 10.json' into ['Cap ', 10, '.json'] for correct sorting."""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


def calculate_grade(percentage):
    """Return numeric grade based on percentage."""
    if 93 <= percentage <= 100:
        return 12
    elif 85 <= percentage < 93:
        return 10
    elif 75 <= percentage < 85:
        return 7
    elif 67 <= percentage < 75:
        return 4
    elif 63 <= percentage < 67:
        return 2
    elif 39 <= percentage < 63:
        return 0
    else:
        return -3


def run_quiz(quiz, quiz_name):
    score = 0
    answers = []

    for i, q in enumerate(quiz, 1):
        print(f"\nQ{i}. {q['question']}")
        for j, option in enumerate(q['options'], 1):
            print(f"  {j}. {option}")

        try:
            choice = int(input("Your answer: ")) - 1
        except ValueError:
            print("Invalid input, skipping...")
            answers.append(
                {"question": q["question"], "chosen": None, "correct": q["options"][q["answer"]]})
            continue

        if choice == q["answer"]:
            print("✅ Correct!")
            score += 1
            correct = True
        else:
            print(f"❌ Wrong! Correct answer: {q['options'][q['answer']]}")
            correct = False

        answers.append({
            "question": q["question"],
            "chosen": q["options"][choice] if 0 <= choice < len(q["options"]) else None,
            "correct": q["options"][q["answer"]],
            "is_correct": correct
        })

    total = len(quiz)
    percentage = round((score / total) * 100, 2)
    grade = calculate_grade(percentage)

    print(f"\nYour score: {score}/{total} ({percentage}%)")
    print(f"Your grade: {grade}")

    # --- Save results ---
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    result_file = os.path.join(
        outputDir, f"result_{quiz_name}_{timestamp}.json")

    result_data = {
        "quiz_name": quiz_name,
        "score": score,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "timestamp": timestamp,
        "answers": answers
    }

    with open(result_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    print(f"\n📝 Results saved to: {result_file}")


if __name__ == "__main__":
    if not os.path.exists(inputDir):
        print(f"Input directory not found: {inputDir}")
        exit(1)

    # List available quiz files
    quizzes = [f for f in os.listdir(inputDir) if f.endswith(".json")]
    quizzes.sort(key=natural_key)

    if not quizzes:
        print("No quiz files found.")
        exit(1)

    print("Available quizzes:")
    for i, qfile in enumerate(quizzes, 1):
        print(f" {i}. {qfile}")

    try:
        choice = int(input("Select quiz number: ")) - 1
        if choice < 0 or choice >= len(quizzes):
            raise ValueError
    except ValueError:
        print("Invalid choice.")
        exit(1)

    quiz_file = os.path.join(inputDir, quizzes[choice])

    # Load quiz from JSON
    with open(quiz_file, "r", encoding="utf-8") as f:
        quiz = json.load(f)

    run_quiz(quiz, quizzes[choice].replace(".json", ""))
