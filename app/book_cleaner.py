import re
try:
    from app.boilerplate_remover import BoilerplateRemover
except ModuleNotFoundError:
    from boilerplate_remover import BoilerplateRemover

class BookCleaner():
        
    def remove_numbers_symbols(self, clean_book):
        """Use regex to remove all non-alphabetical characters (inc. numbers)"""

        # Copy pasted from StackOverflow
        for i in range(len(clean_book)):
            clean_book[i] = re.sub(r"[^a-zA-z0-9]+", ' ', clean_book[i])

        # New variable to avoid confusion
        words_no_symbols = clean_book
        return words_no_symbols

    def format_book(self, clean_book):
        """
        Formats the text such that all words are lower case and any
        whitespace is removed.
        """
        book = self.remove_numbers_symbols(clean_book)

        # Strips whitespace in text and converts to lowercase
        formatted_book = [w.strip().lower() for w in book]

        return formatted_book