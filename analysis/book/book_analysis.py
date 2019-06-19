import csv


class BookAnalysis:

    def __init__(self, book):
        self.book = book
        self.scores_with_sentiment = []
        self.scores_all = []
        self.min_score = 0
        self.max_score = 0
        self.number_of_words = 0
        self.number_of_scored_words = 0
        self.number_of_sentences = 0
        self.avg_of_all_words = 0
        self.avg_of_scored_words = 0
        self.scored_percentage = 0
        self.analysis_name = 'book_analysis'

    def score(self, scored_input_words_df):
        words = self.book.get_words_lower()

        self.scores_with_sentiment = []
        self.scores_all = []

        scores_by_words = scored_input_words_df.get_scores_by_words()

        for word in words:
            word = word.lower()
            if word in scores_by_words:
                score = scores_by_words[word]

                self.scores_with_sentiment.append(score)
                self.scores_all.append(score)
            else:
                self.scores_all.append(0)

        self.number_of_scored_words = len(self.scores_with_sentiment)
        self.number_of_words = len(self.scores_all)
        self.number_of_sentences = len(self.book.get_sentences())
        self.avg_of_scored_words = sum(self.scores_with_sentiment) / self.number_of_scored_words
        self.avg_of_all_words = sum(self.scores_all) / self.number_of_words
        self.min_score = min(self.scores_all)
        self.max_score = max(self.scores_all)
        self.scored_percentage = self.number_of_scored_words / self.number_of_words * 100

    def print(self):
        print("Book title: {}".format(self.book.get_title()))
        print("Book author: {}".format(self.book.get_author()))
        print("Number of all words {}".format(self.number_of_words))
        print("Number of scored words {}".format(self.number_of_scored_words))
        print("Number of sentences {}".format(self.number_of_sentences))
        print("Percentage of scored words: {}%".format(self.scored_percentage))
        print("Min score: {}".format(self.min_score))
        print("Max score: {}".format(self.max_score))
        print("Avg score (for all words, not scored have score 0): {}".format(self.avg_of_all_words))
        print("Avg score (for scored words): {}".format(self.avg_of_scored_words))

    def store_to_file(self, path, book_type, analysis_type, with_header = True):
        file_name = '{}_{}_{}.txt'.format(self.analysis_name, self.book.get_author_name(), self.book.get_title())
        directory = '{}/{}/{}'.format(path, book_type, analysis_type)
        import os
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = '{}/{}'.format(directory, file_name)

        with open(file_path, 'w+') as file:
            score_writer = csv.writer(file)

            if with_header:
                header = ['number_of_words', 'number_of_scored_words', 'percentage_of_scored', 'min_sentiment', 'max_sentiment', 'avg_sentiment_for_all', 'avg_sentiment_for_scored']
                score_writer.writerow(header)

            row = [self.number_of_words, self.number_of_scored_words, self.scored_percentage, self.min_score, self.max_score,
                   self.avg_of_all_words, self.avg_of_scored_words]
            score_writer.writerow(row)
