

class SliceGenerator:

    def __init__(self, slice_size):
        self.slice_size = slice_size

    def get_non_overlapping_windows(self, words):
        return [words[i: i + self.slice_size] for i in range(0, len(words), self.slice_size)]

    def get_overlapping_windows(self, words):
        pass