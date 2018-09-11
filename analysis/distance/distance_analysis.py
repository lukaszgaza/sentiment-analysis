import analysis.general_analysis
import analysis.scoring
import sys

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


class DistanceToWordWithSentimentHigherThan(analysis.general_analysis.GeneralAnalysis,):

    def __init__(self, book, min_sentiment):
        ANALYSIS_NAME = 'distance_to_word_with_sentiment_higher_than_{}'.format(min_sentiment)
        super().__init__(ANALYSIS_NAME, book)
        self.plot_title = 'Distance to word with sentiment higher than {}'.format(min_sentiment)
        self.plot_xlabel = 'Word number'
        self.plot_ylabel = 'Distance'
        self.min_sentiment = min_sentiment

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        source_words = scored_input_words_df.get_scores_by_words()

        self.scores = []
        scores_prev = self._score_helper(words, source_words)
        scores_next = self._score_helper(reversed(words), source_words)
        scores_next = reversed(scores_next)

        all_scores = [scores_prev, scores_next]

        temp_scores = [min(column) for column in zip(*all_scores)]

        for pos in range(len(words)):
            self.scores.append(temp_scores[pos])

        return self.scores

    def _score_helper(self, words, source_words):
        prev_count = sys.maxsize
        scores = []
        for word in words:
            if word in source_words:
                score = source_words[word]
            else:
                score = 0
            if score > self.min_sentiment:
                prev_count = 0
            else:
                if prev_count < sys.maxsize:
                    prev_count += 1

            scores.append(prev_count)

        return scores


class DistanceToWordWithModuloSentimentHigherThan(analysis.general_analysis.GeneralAnalysis,):

    def __init__(self, book, min_sentiment):
        ANALYSIS_NAME = 'distance_to_word_with_modulo_sentiment_higher_than_{}'.format(min_sentiment)
        super().__init__(ANALYSIS_NAME, book)
        self.plot_title = 'Distance to word with modulo sentiment higher than {}'.format(min_sentiment)
        self.plot_xlabel = 'Word number'
        self.plot_ylabel = 'Distance'
        self.min_sentiment = min_sentiment

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        source_words = scored_input_words_df.get_scores_by_words()

        self.scores = []
        scores_prev = self._score_helper(words, source_words)
        scores_next = self._score_helper(reversed(words), source_words)
        scores_next = reversed(scores_next)

        all_scores = [scores_prev, scores_next]

        temp_scores = [min(column) for column in zip(*all_scores)]

        for pos in range(len(words)):
            self.scores.append(temp_scores[pos])

        return self.scores

    def _score_helper(self, words, source_words):
        prev_count = sys.maxsize
        scores = []
        for word in words:
            if word in source_words:
                score = abs(source_words[word])
            else:
                score = 0
            if score > self.min_sentiment:
                prev_count = 0
            else:
                if prev_count < sys.maxsize:
                    prev_count += 1

            scores.append(prev_count)

        return scores


class DistanceToNeutralSentimentAnalysis(analysis.general_analysis.GeneralAnalysis):

    ANALYSIS_NAME = 'distance_to_neutral_sentiment'
    NEUTRAL_SENTIMENT = 5.0

    def __init__(self, book):
        super().__init__(DistanceToNeutralSentimentAnalysis.ANALYSIS_NAME, book)
        self.plot_title = 'Distance to neutral (5.0) sentiment sentiment'
        self.plot_xlabel = 'Word number'
        self.plot_ylabel = 'Distance'

    def score(self, slice_size, scored_input_words_df):
        words = self.book.get_words_lower()
        self.scores = []

        scores_by_words = scored_input_words_df.get_scores_by_words()
        for word in words:
            if word in scores_by_words:
                score = scores_by_words[word]
                self.scores.append(score - DistanceToNeutralSentimentAnalysis.NEUTRAL_SENTIMENT)

        return self.scores
