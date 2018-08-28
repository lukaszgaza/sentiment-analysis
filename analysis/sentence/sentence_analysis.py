import analysis.general_analysis
import analysis.scoring


class SumScoredByScoredCountPerSentenceAnalysisNoNeutralWords(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_scored_count_per_sentence_no_neutral_words'

    def __init__(self, book):
        super().__init__(SumScoredByScoredCountPerSentenceAnalysisNoNeutralWords.ANALYSIS_NAME, book)
        self.plot_title = 'Sentiment as sum of scored words in a sentence by count of scored words'
        self.plot_xlabel = 'Sentence number'
        self.plot_ylabel = 'Sentiment'

    def score(self, slice_size, scored_input_words_df):
        sentences = self.book.get_sentences()

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_scored_words(scored_input_words_df, analysis.scoring.NEUTRAL_WORD_FILTER), sentences))

        return self.scores
