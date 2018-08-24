
class Input:

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

    def get_non_stop_words(self, scored_input_words_df):
        AVERAGE_SCORE = 5.0
        DELTA = 1.0

        text_without_stop_words = []
        scores_by_words = scored_input_words_df.get_scores_by_words()
        for word in self.get_scored_words(scored_input_words_df):
            score = scores_by_words[word]

            if score <= AVERAGE_SCORE - DELTA or score >= AVERAGE_SCORE + DELTA:
                text_without_stop_words.append(word)

        return text_without_stop_words