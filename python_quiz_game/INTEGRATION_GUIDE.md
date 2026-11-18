# Integration Guide

The backend is in `quiz_engine.py`. A Python-based interface can import its functions.

```python
from quiz_engine import (
    get_public_questions,
    check_answer_by_index,
    get_explanation,
    get_quiz_results
)
```

## 1. Get the questions

```python
questions = get_public_questions()
```

Each item contains an `id`, `question`, and `options`. It does not expose the answer.

## 2. Check an answer

```python
is_correct = check_answer_by_index(question_id, selected_answer)
```

`selected_answer` should be `"A"`, `"B"`, `"C"`, or `"D"`.

## 3. Get an explanation

```python
explanation = get_explanation(question_id)
```

## 4. Prepare the final result

Track the number of correct answers in the interface, then call:

```python
results = get_quiz_results(player_name, score, total_questions)
```

The returned dictionary includes the player's name, correct and incorrect counts, percentage, and feedback.

## Important integration note

These imports work when the interface runs in Python in the same project environment. If the interface is a browser application (for example, HTML/CSS/JavaScript or React), it cannot directly import a local Python file. A Python API layer will be needed between the browser and this backend. Confirm the interface technology before merging.
