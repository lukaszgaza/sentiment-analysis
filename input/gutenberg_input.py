import nltk
from input import general_input


class GutenbergInput(general_input.Input):

    def __init__(self, gutenberg_name, title):
        self.gutenberg_name = gutenberg_name
        self.title = title
        self.author = ''

    def get_raw_text(self):
        return nltk.corpus.gutenberg.raw(self.gutenberg_name)

    def get_sentences(self):
        return nltk.corpus.gutenberg.sents(self.gutenberg_name)

    def get_words(self):
        return nltk.corpus.gutenberg.words(self.gutenberg_name)