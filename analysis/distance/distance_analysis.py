import analysis.general_analysis
import analysis.scoring


class DistanceToPreviousWordWithSentimentAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'distance_to_previous_word_with_sentiment'

    def __init__(self, book):
        super().__init__(DistanceToPreviousWordWithSentimentAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Distance to previous word with sentiment'
        self.plot_xlabel = 'Word number'
        self.plot_ylabel = 'Distance'

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        prev_count = 0
        self.scores = []

        source_words = scored_input_words_df.get_scores_by_words()
        for word in words:
            if word in source_words:
                self.scores.append(prev_count)
                prev_count = 0
            else:
                prev_count += 1

        return self.scores
