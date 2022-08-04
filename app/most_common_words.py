from collections import Counter
try:
    from app.book_cleaner import BookCleaner
except ModuleNotFoundError:
    from book_cleaner import BookCleaner

class MostFrequentWords():

    def common_words(self, book_common):
        """
        Get the most common words in the list and return as a dictionary with the word
        and frequency with which it appears in the list.
        """

        #Most common words
        most_common_words = Counter(book_common).most_common(20)

        #Convert to a dictionary
        dict_common_words = dict(most_common_words)

        print("Dictionary of most common words and their frequency:", dict_common_words)

        return dict_common_words