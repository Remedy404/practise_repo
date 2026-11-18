from quiz_game import get_questions

questions = get_questions()
print("\n========== PYTHON QUIZ ANSWER KEY ==========\n")
for number, question in enumerate(questions, start=1):
    answer = question["answer"]
    answer_text = question["options"][answer]
    print(f"{number}. {question['question']}")
    print(f"   Answer: {answer} - {answer_text}\n")
