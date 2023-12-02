import pkg_resources

from symspellpy import SymSpell

class Orthograph():
    def __init__(self) -> None:
        self.sym_spell = SymSpell()
        self.dictionnary, self.bigram_dict =\
            self.load_dict()

    def load_dict(self):
        dictionary_path = pkg_resources.resource_filename(
            "symspellpy",
            "frequency_dictionary_en_82_765.txt"
        )
        bigram_path = pkg_resources.resource_filename(
            "symspellpy",
            "frequency_bigramdictionary_en_243_342.txt"
        )
        dictionnary = self.sym_spell.load_dictionary(
            dictionary_path,
            term_index=0,
            count_index=1
        )
        bigram_dict = self.sym_spell.load_bigram_dictionary(
            bigram_path,
            term_index=0,
            count_index=2
        )
        return dictionnary, bigram_dict
    
    def correct_sentence(self, sentence):
        suggestions = self.sym_spell.lookup_compound(sentence)
        return suggestions[0]._term