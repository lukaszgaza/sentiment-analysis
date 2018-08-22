import pandas as pd


class ScoredWords:

    def __init__(self, input_file_path):
        self.words = pd.read_csv(input_file_path)