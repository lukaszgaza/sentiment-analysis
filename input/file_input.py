from input import general_input
import io
from nltk import word_tokenize, sent_tokenize


class FileInput(general_input.Input):

    def __init__(self, path, title):
        self.path = path
        self.title = title
        self.author = ''
        self.raw = io.open(path, mode="r", encoding="utf-8").read()

    def get_raw_text(self):
        return self.raw

    def get_sentences(self):
        sentences = sent_tokenize(self.raw)
        return [word_tokenize(sentence) for sentence in sentences]

    def get_words(self):
        return word_tokenize(self.raw)