import unittest

from text.text import Text


class TestText(unittest.TestCase):
    def setUp(self) -> None:
        self.test_object = Text()

    def test_clean_text(self):
        """
        Clean text
        """
        # Given
        raw_text = "My beautiful text!"
        expected_result = "my beautiful text"

        # Acts
        op_result = self.test_object.clean_text(raw_text)

        # Asserts
        self.assertEqual(op_result,expected_result)

    def test_word_tokenization(self):
        """
        Clean text
        """
        # Given
        raw_text = "my beautiful text"
        expected_result = ['my','beautiful','text']

        # Acts
        op_result = self.test_object.word_tokenization(raw_text)

        # Asserts
        self.assertEqual(op_result,expected_result)

    def test_word_lemmitization(self):
        """
        Clean text
        """
        # Given
        raw_text = ["my", "beautiful", "loving", "text"]
        expected_result = ['my','beautiful','love','text']

        # Acts
        op_result = self.test_object.word_lemmitization(raw_text)

        # Asserts
        self.assertEqual(op_result,expected_result)

