from collections import Counter
try:
    from app.book_cleaner import BookCleaner
except ModuleNotFoundError:
    from book_cleaner import BookCleaner

class MostFrequentWords():
    def __init__(self, url_book):
        self.bc = BookCleaner(url_book)

    def common_words(self):
        book_common = self.bc.sort_alphabetical()
        print('Number of words:', len(book_common))

        #Most common words
        most_common_words = Counter(book_common).most_common(20)

        #Convert to a dictionary
        dict_common_words = dict(most_common_words)

        print("Dictionary of most common words and their frequency:", dict_common_words)

        return dict_common_words

