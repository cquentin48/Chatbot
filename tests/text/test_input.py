import unittest
import os

import pandas as pd
from pandas import testing as tm

from text.input import Input


class TestInput(unittest.TestCase):
    def get_res_folder(self) -> str:
        project_root_path = os.path.dirname(os.path.abspath(__file__))
        return f"{project_root_path}".replace("/tests/text","/tests/res")
    
    def test_init_single_file(self):
        # Given
        file_name = 'test_raw.csv'
        file_path = f"{self.get_res_folder()}/{file_name}"
        expected_result = {
            "questions":['how','are','you'],
            "answers":['you','are','loving','today']
        }
        obj:Input = Input(file_path,"questions","answers")

        # Acts
        op_result_question = obj.tokenize_data('questions')
        op_result_answers = obj.tokenize_data('answers')

        # Asserts
        self.assertEqual(op_result_answers.tolist()[0],expected_result['answers'])
        self.assertEqual(op_result_question.tolist()[0],expected_result['questions'])
