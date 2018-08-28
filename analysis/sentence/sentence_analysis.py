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


class SumScoredByScoredCountPerSentenceAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_scored_count_per_sentence'

    def __init__(self, book):
        super().__init__(SumScoredByScoredCountPerSentenceAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Sentiment as sum of scored words in a sentence by count of scored words'
        self.plot_xlabel = 'Sentence number'
        self.plot_ylabel = 'Sentiment'

    def score(self, slice_size, scored_input_words_df):
        sentences = self.book.get_sentences()

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_scored_words(scored_input_words_df, analysis.scoring.TRUE_FILTER), sentences))

        return self.scores


class SumScoredByAllCountPerSentenceAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_all_count_per_sentence'

    def __init__(self, book):
        super().__init__(SumScoredByAllCountPerSentenceAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Sentiment as sum of scored words in a sentence by count of all words'
        self.plot_xlabel = 'Sentence number'
        self.plot_ylabel = 'Sentiment'

    def score(self, slice_size, scored_input_words_df):
        sentences = self.book.get_sentences()

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_all_words(scored_input_words_df, analysis.scoring.TRUE_FILTER), sentences))

        return self.scores


class SumScoredPerSentenceAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_per_sentence'

    def __init__(self, book):
        super().__init__(SumScoredPerSentenceAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Sentiment as sum of scored words in a sentence'
        self.plot_xlabel = 'Sentence number'
        self.plot_ylabel = 'Sentiment'

    def score(self, slice_size, scored_input_words_df):
        sentences = self.book.get_sentences()

        self.scores = list(map(analysis.scoring.score_slice_as_sum_of_all_words(scored_input_words_df, analysis.scoring.TRUE_FILTER), sentences))

        return self.scores


class NumberOfWordsWithSentimentPerSentenceAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'number_of_words_with_sentiment_per_sentence'

    def __init__(self, book):
        super().__init__(NumberOfWordsWithSentimentPerSentenceAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Number of words with sentiment per sentence'
        self.plot_xlabel = 'Sentence number'
        self.plot_ylabel = 'Number of words with sentiment'

    def score(self, slice_size, scored_input_words_df):
        sentences = self.book.get_sentences()

        self.scores = list(map(analysis.scoring.score_slice_as_count_of_scored_words(scored_input_words_df,
                                                                                   analysis.scoring.TRUE_FILTER), sentences))

        return self.scores


class NumberOfWordsPerSentenceAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'number_of_words_per_sentence'

    def __init__(self, book):
        super().__init__(NumberOfWordsPerSentenceAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Number of words per sentence'
        self.plot_xlabel = 'Sentence number'
        self.plot_ylabel = 'Number of words'

    def score(self, slice_size, scored_input_words_df):
        sentences = self.book.get_sentences()

        self.scores = list(map(len, sentences))

        return self.scores