import csv

class GeneralAnalysis:

    def __init__(self, analysis_name, book):
        self.analysis_name = analysis_name
        self.book = book
        self.scores = []

    def score(self, slice_size, scored_input_words_df):
        pass

    def store_to_file(self, path, with_slice_number = False, with_header = True):
        file_name = '{}_{}_{}.txt'.format(self.book.get_author(), self.book.get_title(), self.analysis_name)
        file_path = '{}/{}'.format(path, file_name)

        slice_number = 1
        with open(file_path, 'w+') as file:
            score_writer = csv.writer(file)

            if with_header:
                if with_slice_number:
                    header = ['slice', 'score']
                else:
                    header = ['score']

                score_writer.writerow(header)

            for score in self.scores:
                if with_slice_number:
                    row = [slice_number, score]
                else:
                    row = [score]

                score_writer.writerow(row)
                slice_number += 1
