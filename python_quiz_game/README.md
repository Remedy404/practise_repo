# Python Quiz Game

A beginner-friendly Python quiz game covering functions, basic data types, conditional statements, and Python fundamentals.

## Topics and question count
- Functions: 15 questions
- Basic data types (`int`, `float`, `str`, `bool`): 15 questions
- Conditional statements: 12 questions
- Python fundamentals: 8 questions
- Total: 50 questions

## Run the game
Open a terminal in this folder and run:

```bash
python3 quiz_game.py
```

## Show the answer key

```bash
python3 show_answers.py
```

## Run all automated tests

```bash
python3 -m unittest discover -v
```

## Main files
- `quiz_game.py` — standalone playable quiz.
- `quiz_engine.py` — reusable backend functions for another interface.
- `show_answers.py` — displays all correct answers.
- `test_quiz.py` — tests the standalone quiz.
- `test_quiz_engine.py` — tests the reusable backend.
- `INTEGRATION_GUIDE.md` — explains how another interface can use the backend.
- `quiz_game_backup.py` — backup copy of the standalone game.

## Backend functions
`quiz_engine.py` provides:
- `get_questions()`
- `get_public_questions()`
- `validate_answer(answer)`
- `check_answer(question, player_answer)`
- `check_answer_by_index(question_index, player_answer)`
- `get_explanation(question_index)`
- `calculate_percentage(score, total)`
- `get_feedback(percentage)`
- `get_quiz_results(player_name, score, total)`

The public question function deliberately leaves out the correct answer and explanation.
