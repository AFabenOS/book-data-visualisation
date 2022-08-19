from cgi import test
import re

try:
    from app.boilerplate_remover import BoilerplateRemover
except ModuleNotFoundError:
    from boilerplate_remover import BoilerplateRemover


class BookCleaner():
        
    def remove_nonalphanumeric(self, book_removed_bp):
        """Use regex to remove all non-alphabetical characters (inc. numbers)"""

        # Copy pasted from StackOverflow
        for i in range(len(book_removed_bp)):
            book_removed_bp[i] = re.sub(r"[^a-zA-z0-9]+", ' ', book_removed_bp[i])
        print('test', book_removed_bp)

        # New variable to avoid confusion
        words_no_symbols = book_removed_bp
        return words_no_symbols

    def format_book(self, book_removed_bp):
        """
        Formats the text such that all words are lower case and any
        whitespace is removed.
        """
        book = self.remove_nonalphanumeric(book_removed_bp)

        # Strips whitespace in text and converts to lowercase
        formatted_book = [w.strip().lower() for w in book]
        print(formatted_book)
        return formatted_book

# test_list = ['a', ',', 'b;;;', 'c', 'd.']
# bc = BookCleaner()
# bc.format_book(test_list)