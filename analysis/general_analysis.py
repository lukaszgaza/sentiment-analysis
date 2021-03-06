import csv
import matplotlib.pyplot as plt

class GeneralAnalysis:

    def __init__(self, analysis_name, book):
        self.analysis_name = analysis_name
        self.book = book
        self.scores = []
        self.plot_title = ''
        self.plot_xlabel = ''
        self.plot_ylabel = ''

    def score(self, slice_size, scored_input_words_df):
        pass

    def store_to_file(self, path, book_type, analysis_type, with_slice_number = False, with_header = True):
        file_name = '{}_{}_{}.txt'.format(self.analysis_name, self.book.get_author_name(), self.book.get_title())
        directory = '{}/{}/{}'.format(path, book_type, analysis_type)
        file_path = '{}/{}'.format(directory, file_name)

        import os
        if not os.path.exists(directory):
            os.makedirs(directory)

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

    def plot(self):
        plt.title(self.plot_title)
        plt.xlabel(self.plot_xlabel)
        plt.ylabel(self.plot_ylabel)
        plt.plot(self.scores)
        plt.show()