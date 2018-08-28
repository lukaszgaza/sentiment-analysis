import nltk
from input import general_input
from nltk import word_tokenize


class GutenbergInput(general_input.Input):

    def __init__(self, gutenberg_name, author, title):
        self.gutenberg_name = gutenberg_name
        self.author = author
        self.title = title

    def get_raw_text(self):
        return nltk.corpus.gutenberg.raw(self.gutenberg_name)

    def get_sentences(self):
        return [word_tokenize(sentence) for sentence in nltk.corpus.gutenberg.sents(self.gutenberg_name)]

    def get_words(self):
        return nltk.corpus.gutenberg.words(self.gutenberg_name)