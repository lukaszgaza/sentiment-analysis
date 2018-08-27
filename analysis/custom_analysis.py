import analysis.general_analysis
import analysis.scoring
import analysis.slice_generator


class SumScoredByScoredCountAnalysisNoNeutralWords(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_scored_count_no_neutral_words'

    def __init__(self, book):
        super().__init__(SumScoredByScoredCountAnalysisNoNeutralWords.ANALYSIS_NAME, book)

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        slices = analysis.slice_generator.SliceGenerator(slice_size).get_non_overlapping_windows(words)

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_scored_words(scored_input_words_df, analysis.scoring.NEUTRAL_WORD_FILTER), slices))

        return self.scores


# NOT TESTED BELOW
class SumScoredByScoredCountAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_scored_count'

    def __init__(self, book):
        super().__init__(SumScoredByAllCountAnalysis.ANALYSIS_NAME, book)
        self.scores = []

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        slices = analysis.slice_generator.SliceGenerator(slice_size).get_non_overlapping_windows(words)

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_scored_words(scored_input_words_df, analysis.scoring.TRUE_FILTER), slices))

        return self.scores





class SumScoredByAllCountAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_all_count'

    def __init__(self, book):
        super().__init__(SumScoredByAllCountAnalysis.ANALYSIS_NAME, book)
        self.scores = []

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        slices = analysis.slice_generator.SliceGenerator(slice_size).get_non_overlapping_windows(words)

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_all_words(scored_input_words_df), slices))

        return self.scores


class SumScoredByAllCountAnalysisNoNeutralWords(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'sum_scored_by_all_count_no_neutral_words'

    def __init__(self, book):
        super().__init__(SumScoredByAllCountAnalysisNoNeutralWords.ANALYSIS_NAME, book)
        self.scores = []

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        non_neutral_words = self.book.get_non_neutral_words(scored_input_words_df)
        slices = analysis.slice_generator.SliceGenerator(slice_size).get_non_overlapping_windows(words)

        self.scores = list(map(analysis.scoring.score_slice_as_avg_of_all_words(scored_input_words_df), slices))

        return self.scores
