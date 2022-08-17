from collections import Counter
try:
    from app.book_cleaner import BookCleaner
except ModuleNotFoundError:
    from book_cleaner import BookCleaner
else:
    print("Error: A Module could not be imported correctly.")

class MostFrequentWords():

    def get_frequent_words(self, formatted_book):
        """
        Get the most common words in the list and return as a dictionary with the word
        and frequency with which it appears in the list.
        """

        #Most common words
        most_frequent_words = Counter(formatted_book).most_common(20)

        #Convert to a dictionary
        dict_frequent_words = dict(most_frequent_words)

        print("Most frequent words and how often they appear:", dict_frequent_words)

        return dict_frequent_words