import pandas as pd
import matplotlib.pyplot as plt


class ScoredWords:

    def __init__(self, input_file_path):
        self.words = pd.read_csv(input_file_path)

    def get_words_df(self):
        return self.words

    def get_words(self):
        return [word for word in self.words['Word']]

    def hist(self):
        plt.hist(self.words["Average"], bins=10)
        plt.xlabel("Sentiment")
        plt.ylabel("# of words")
        plt.show()