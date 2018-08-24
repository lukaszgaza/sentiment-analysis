
def score_slice_as_avg_of_scored_words(slice, scored_input_words_df):
    total_score = 0.0
    count = 0

    if len(slice) == 0:
        return 0

    scores_by_words = scored_input_words_df.get_scores_by_words()

    for word in slice:
        word = word.lower()
        words_score = scores_by_words[word]

        total_score += words_score
        count += 1

    return float(total_score) / count


def score_slice_as_sum_of_scored_words(slice, scored_input_words_df):
    total_score = 0.0

    if len(slice) == 0:
        return 0

    scores_by_words = scored_input_words_df.get_scores_by_words()

    for word in slice:
        word = word.lower()
        words_score = scores_by_words[word]

        total_score += words_score

    return total_score


def score_slice_as_avg_of_all_words(slice, scored_input_words_df):

    # non-scored words have score 0
    if len(slice) == 0:
        return 0

    return float(score_slice_as_sum_of_scored_words(slice, scored_input_words_df)) / len(slice)