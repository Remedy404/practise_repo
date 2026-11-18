import unittest
from unittest.mock import patch
from quiz_game import get_questions, get_player_answer, display_results

class TestQuizGame(unittest.TestCase):
    def test_questions_count(self):
        self.assertEqual(len(get_questions()), 50)

    def test_question_has_four_options(self):
        for question in get_questions():
            self.assertEqual(len(question["options"]), 4)

    def test_question_has_valid_answer(self):
        for question in get_questions():
            self.assertIn(question["answer"], ("A", "B", "C", "D"))

    def test_question_has_explanation(self):
        for question in get_questions():
            self.assertTrue(question["explanation"])

    @patch("builtins.input", side_effect=["x", "A"])
    @patch("builtins.print")
    def test_answer_validation(self, mock_print, mock_input):
        self.assertEqual(get_player_answer(), "A")

    @patch("builtins.input", return_value="  b ")
    def test_answer_is_normalized(self, mock_input):
        self.assertEqual(get_player_answer(), "B")

    @patch("builtins.print")
    def test_results_display(self, mock_print):
        display_results("Alex", 5, 10)
        self.assertTrue(mock_print.called)

if __name__ == "__main__":
    unittest.main()
