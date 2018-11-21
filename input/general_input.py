
class Input:
    def get_title(self):
        return self.title

    def get_author(self):
        return str(self.author)

    def get_raw_text(self):
        pass

    def get_sentences(self):
        pass

    def get_words(self):
        pass

    def get_words_lower(self):
        return [word.lower() for word in self.get_words()]

    def get_scored_words(self, scored_input_words_df):
        return [word for word in self.get_words_lower() if word in scored_input_words_df.get_words()]
