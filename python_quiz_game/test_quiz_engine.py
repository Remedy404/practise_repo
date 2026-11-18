import unittest
from quiz_engine import (
    get_questions, validate_answer, check_answer, calculate_percentage,
    get_feedback, get_quiz_results, get_public_questions,
    check_answer_by_index, get_explanation
)

class TestQuizEngine(unittest.TestCase):
    def test_question_structure(self):
        for question in get_questions():
            self.assertIn("question", question)
            self.assertIn("options", question)
            self.assertIn("answer", question)
            self.assertIn("explanation", question)
            self.assertEqual(set(question["options"]), {"A", "B", "C", "D"})

    def test_questions_count(self):
        self.assertEqual(len(get_questions()), 50)

    def test_valid_answers(self):
        for answer in ("A", "B", "C", "D", "a", " b "):
            self.assertTrue(validate_answer(answer))

    def test_wrong_answer(self):
        self.assertFalse(validate_answer("Z"))

    def test_quiz_results(self):
        result = get_quiz_results("Alex", 8, 10)
        self.assertEqual(result["percentage"], 80.0)
        self.assertEqual(result["correct_answers"], 8)
        self.assertEqual(result["incorrect_answers"], 2)

    def test_check_answer_correct(self):
        question = get_questions()[0]
        self.assertTrue(check_answer(question, question["answer"]))

    def test_check_answer_incorrect(self):
        question = get_questions()[0]
        wrong = next(a for a in "ABCD" if a != question["answer"])
        self.assertFalse(check_answer(question, wrong))

    def test_invalid_answer_raises(self):
        with self.assertRaises(ValueError):
            check_answer(get_questions()[0], "Z")

    def test_percentage(self):
        self.assertEqual(calculate_percentage(5, 10), 50.0)

    def test_zero_total_raises(self):
        with self.assertRaises(ValueError):
            calculate_percentage(0, 0)

    def test_feedback(self):
        self.assertIn("Excellent", get_feedback(90))

    def test_public_questions(self):
        questions = get_public_questions()
        self.assertEqual(len(questions), 50)
        self.assertIn("id", questions[0])
        self.assertIn("question", questions[0])
        self.assertIn("options", questions[0])
        self.assertNotIn("answer", questions[0])
        self.assertNotIn("explanation", questions[0])

    def test_answer_by_index(self):
        questions = get_questions()
        self.assertTrue(check_answer_by_index(0, questions[0]["answer"]))

    def test_explanation(self):
        self.assertTrue(get_explanation(0))

if __name__ == "__main__":
    unittest.main()
