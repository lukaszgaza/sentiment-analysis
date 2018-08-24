AVERAGE_SCORE = 5.0
DELTA = 1.0
NEUTRAL_WORD_FILTER = lambda score: score <= AVERAGE_SCORE - DELTA or score >= AVERAGE_SCORE + DELTA
TRUE_FILTER = lambda score: True


def score_slice_as_avg_of_scored_words(scored_input_words_df, filter):

    scores_by_words = scored_input_words_df.get_scores_by_words()

    def score_slice_as_avg_of_scored_words_helper(slice):
        total_score = 0.0
        count = 0

        for word in slice:
            if word in scores_by_words:
                score = scores_by_words[word]
                if NEUTRAL_WORD_FILTER(score):
                    total_score += score
                    count += 1

        if count == 0:
            return 0
        return total_score / count

    return score_slice_as_avg_of_scored_words_helper




# BELOW NOT TESTED
def score_slice_as_sum_of_scored_words(scored_input_words_df):

    scores_by_words = scored_input_words_df.get_scores_by_words()

    def score_slice_as_sum_of_scored_words_helper(slice):

        if len(slice) == 0:
            return 0

        total_score = 0.0

        for word in slice:
            word = word.lower()

            if word in scores_by_words:
                word_score = scores_by_words[word]
                total_score += word_score

        return total_score

    return score_slice_as_sum_of_scored_words_helper


def score_slice_as_avg_of_all_words(scored_input_words_df):

    # non-scored words have score 0

    scores_by_words = scored_input_words_df.get_scores_by_words()

    def score_slice_as_avg_of_all_words_helper(slice):

        if len(slice) == 0:
            return 0

        total_score = 0.0

        for word in slice:
            word = word.lower()
            if word in scores_by_words:
                word_score = scores_by_words[word]
                total_score += word_score

        return float(total_score) / len(slice)

    return score_slice_as_avg_of_all_words_helper
