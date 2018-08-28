import analysis.general_analysis
import analysis.scoring
import analysis.slice_generator


class SumScoredByScoredCountAnalysisNoNeutralWords(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_scored_count_no_neutral_words'

    def __init__(self, book):
        super().__init__(SumScoredByScoredCountAnalysisNoNeutralWords.ANALYSIS_NAME, book)
        self.plot_title = 'Sentiment as sum of scored words in a slice by count of scored words'
        self.plot_xlabel = 'Slice number'
        self.plot_ylabel = 'Sentiment'

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        slices = analysis.slice_generator.SliceGenerator(slice_size).get_non_overlapping_windows(words)

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_scored_words(scored_input_words_df, analysis.scoring.NEUTRAL_WORD_FILTER), slices))

        return self.scores


class SumScoredByScoredCountAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_scored_count'

    def __init__(self, book):
        super().__init__(SumScoredByScoredCountAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Sentiment as sum of scored words in a slice by count of scored words'
        self.plot_xlabel = 'Slice number'
        self.plot_ylabel = 'Sentiment'

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        slices = analysis.slice_generator.SliceGenerator(slice_size).get_non_overlapping_windows(words)

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_scored_words(scored_input_words_df, analysis.scoring.TRUE_FILTER), slices))

        return self.scores


class SumScoredByAllCountAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_all_count'

    def __init__(self, book):
        super().__init__(SumScoredByAllCountAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Sentiment as sum of scored words in a slice by count of all words'
        self.plot_xlabel = 'Slice number'
        self.plot_ylabel = 'Sentiment'

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        slices = analysis.slice_generator.SliceGenerator(slice_size).get_non_overlapping_windows(words)

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_all_words(scored_input_words_df, analysis.scoring.TRUE_FILTER), slices))

        return self.scores


class SumScoredAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored'

    def __init__(self, book):
        super().__init__(SumScoredAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Sentiment as sum of scored words in a slice'
        self.plot_xlabel = 'Slice number'
        self.plot_ylabel = 'Sentiment'

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        slices = analysis.slice_generator.SliceGenerator(slice_size).get_non_overlapping_windows(words)

        self.scores = list(map(analysis.scoring.score_slice_as_sum_of_all_words(scored_input_words_df, analysis.scoring.TRUE_FILTER), slices))

        return self.scores


class NumberOfWordsWithSentimentPerSliceAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'number_of_words_with_sentiment_per_slice'

    def __init__(self, book):
        super().__init__(NumberOfWordsWithSentimentPerSliceAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Number of words with sentiment per slice'
        self.plot_xlabel = 'Slice number'
        self.plot_ylabel = 'Number of words with sentiment'

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        slices = analysis.slice_generator.SliceGenerator(slice_size).get_non_overlapping_windows(words)

        self.scores = list(map(analysis.scoring.score_slice_as_count_of_scored_words(scored_input_words_df,
                                                                                   analysis.scoring.TRUE_FILTER), slices))

        return self.scores
