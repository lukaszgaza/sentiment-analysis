AVERAGE_SCORE = 0.0
DELTA = 1.0
NEUTRAL_WORD_FILTER = lambda score: score <= AVERAGE_SCORE - DELTA or score >= AVERAGE_SCORE + DELTA
TRUE_FILTER = lambda score: True
NEGATIVE_FILTER = lambda score: score < AVERAGE_SCORE
POSITIVE_FILTER = lambda score: score > AVERAGE_SCORE

import math


def score_slice_as_avg_of_scored_words(scored_input_words_df, filter_fun):

    scores_by_words = scored_input_words_df.get_scores_by_words()

    def score_slice_as_avg_of_scored_words_helper(slice):
        total_score = 0.0
        count = 0

        for word in slice:
            # TODO - remove lowering from here? and all the below?
            word = word.lower()
            if word in scores_by_words:
                score = scores_by_words[word]
                if filter_fun(score):
                    total_score += score
                    count += 1

        if count == 0:
            return 0
        return total_score / count

    return score_slice_as_avg_of_scored_words_helper


def score_slice_as_avg_of_all_words(scored_input_words_df, filter_fun):
    scores_by_words = scored_input_words_df.get_scores_by_words()

    def score_slice_as_avg_of_all_words_helper(slice):
        total_score = 0.0

        if len(slice) == 0:
            return 0

        for word in slice:
            # TODO - remove lowering from here? and all the below?
            word = word.lower()
            if word in scores_by_words:
                score = scores_by_words[word]
                if filter_fun(score):
                    total_score += score

        return total_score / len(slice)

    return score_slice_as_avg_of_all_words_helper


def score_slice_as_sum_of_all_words(scored_input_words_df, filter_fun):
    scores_by_words = scored_input_words_df.get_scores_by_words()

    def score_slice_as_sum_of_all_words_helper(slice):
        total_score = 0.0

        if len(slice) == 0:
            return 0

        for word in slice:
            # TODO - remove lowering from here? and all the below?
            word = word.lower()
            if word in scores_by_words:
                score = scores_by_words[word]
                if filter_fun(score):
                    total_score += score

        return total_score

    return score_slice_as_sum_of_all_words_helper


def score_slice_as_count_of_scored_words(scored_input_words_df, filter_fun):

    scores_by_words = scored_input_words_df.get_scores_by_words()

    def score_slice_as_count_of_scored_words_helper(slice):
        count = 0

        for word in slice:
            # TODO - remove lowering from here? and all the below?
            word = word.lower()
            if word in scores_by_words:
                score = scores_by_words[word]

                if filter_fun(score):
                    count += 1

        return count

    return score_slice_as_count_of_scored_words_helper


def score_slice_as_sum_of_modulo_of_all_words(scored_input_words_df, filter_fun):
    scores_by_words = scored_input_words_df.get_scores_by_words()

    def score_slice_as_sum_of_modulo_of_all_words_helper(slice):
        total_score = 0.0

        if len(slice) == 0:
            return 0

        for word in slice:
            # TODO - remove lowering from here? and all the below?
            word = word.lower()
            if word in scores_by_words:
                score = math.fabs(scores_by_words[word])
                if filter_fun(score):
                    total_score += score

        return total_score

    return score_slice_as_sum_of_modulo_of_all_words_helper

