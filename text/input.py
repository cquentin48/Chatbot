import pandas as pd

from .text import Text

class Input():

    def __init__(self, file_path, question_col:str, answer_col: str):
        self.text = Text()
        if isinstance(file_path,str):
            self.raw_df = self.load_data(file_path, question_col, answer_col)
        elif all(isinstance(single_file_path,str) for single_file_path in file_path):
            raw_df = []
            for single_input in file_path:
                new_raw_df = self.load_data(single_input, question_col, answer_col)
                raw_df.append(new_raw_df)
            self.raw_df = pd.concat(raw_df)

    def load_data(self, file_path:str, question_col:str, answer_col:str):
        df = pd.read_csv(file_path, sep=';')
        df[question_col] = df[question_col].apply(self.text.clean_text)
        df[answer_col] = [self.text.clean_text(single_text) for single_text in df[answer_col].tolist()]
        return df
    
    def tokenize_data(self, col_name):
        return self.raw_df[col_name].apply(self.text.word_tokenization)
    
    def spell_correction(self, col_name):



