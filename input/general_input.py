
class Input:

    def get_raw_text(self):
        pass

    def get_sentences(self):
        pass

    def get_words(self):
        pass

    def get_words_lower(self):
        return [word.lower() for word in self.get_words()]