from nltk.corpus import wordnet
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, RegexpTokenizer

class Text():
    def __init__(self):
        self.st = SnowballStemmer('english')
        self.lem = WordNetLemmatizer()

    def clean_text(self, text_input: str) -> str:
        """Text cleaning

        Args:
            text_input (str): raw text to be cleaned

        Returns:
            str: Text without capital cases, no punctuation and no stop words
        """
        lower_case = text_input.lower().strip()
        punctuation_removed = ' '.join(self.remove_punctuation(lower_case))
        no_stop_words = ''.join(self.st.stem(punctuation_removed)) if punctuation_removed not in self.st.stopwords else ''
        return no_stop_words
    
    def remove_punctuation(self, text_input:str) -> str:
        """Remove every punctuation from text input

        Args:
            text_input (str): raw text to be cleaned

        Returns:
            str: text without punctuation
        """
        tokenizer = RegexpTokenizer(r'\w+')
        return tokenizer.tokenize(text_input)
    
    def word_tokenization(self, text_input: str) -> list[str]:
        """Sentence tokenization

        Args:
            text_input (str): raw to be tokenized

        Returns:
            list[str]: sentence split into an array.
        """
        return word_tokenize(text_input)
    
    def word_lemmitization(self, text_input:[str]) -> list[str]:
        return [self.lem.lemmatize(word, wordnet.VERB) for word in text_input]