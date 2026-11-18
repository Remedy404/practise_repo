from quiz_game import get_questions

def validate_answer(answer):
    """Check whether an answer is a valid quiz option."""
    if not isinstance(answer, str):
        return False
    return answer.strip().upper() in ("A", "B", "C", "D")

def check_answer(question, player_answer):
    """Check whether the player's answer is correct."""
    if not validate_answer(player_answer):
        raise ValueError("Answer must be A, B, C or D.")
    return player_answer.strip().upper() == question["answer"]

def calculate_percentage(score, total):
    """Calculate the quiz score as a percentage."""
    if not isinstance(score, int) or not isinstance(total, int):
        raise TypeError("Score and total must be integers.")
    if total <= 0:
        raise ValueError("Total questions must be greater than zero.")
    if score < 0 or score > total:
        raise ValueError("Score must be between zero and total.")
    return round((score / total) * 100, 1)

def get_feedback(percentage):
    """Return performance feedback based on percentage."""
    if percentage >= 80:
        return "Excellent work! You have done very well."
    elif percentage >= 60:
        return "Good job! Keep practising."
    elif percentage >= 40:
        return "Nice effort! There is still room to improve."
    return "Keep learning. Every attempt helps you improve."

def get_quiz_results(player_name, score, total):
    """Generate a structured summary of quiz results."""
    percentage = calculate_percentage(score, total)
    return {
        "player_name": player_name,
        "total_questions": total,
        "correct_answers": score,
        "incorrect_answers": total - score,
        "percentage": percentage,
        "feedback": get_feedback(percentage)
    }

def get_public_questions():
    """Return questions and options without exposing answers."""
    public_questions = []
    for index, question in enumerate(get_questions()):
        public_questions.append({
            "id": index,
            "question": question["question"],
            "options": question["options"]
        })
    return public_questions

def check_answer_by_index(question_index, player_answer):
    """Check an answer using the question's ID."""
    questions = get_questions()
    if not isinstance(question_index, int):
        raise TypeError("Question ID must be an integer.")
    if question_index < 0 or question_index >= len(questions):
        raise ValueError("Invalid question ID.")
    return check_answer(questions[question_index], player_answer)

def get_explanation(question_index):
    """Return the explanation for a question."""
    questions = get_questions()
    if not isinstance(question_index, int):
        raise TypeError("Question ID must be an integer.")
    if question_index < 0 or question_index >= len(questions):
        raise ValueError("Invalid question ID.")
    return questions[question_index]["explanation"]
