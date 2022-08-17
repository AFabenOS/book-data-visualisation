import re
try:
    from app.boilerplate_remover import BoilerplateRemover
except ModuleNotFoundError:
    from boilerplate_remover import BoilerplateRemover
else:
    print("Error: A Module could not be imported correctly.")

class BookCleaner():
        
    def remove_numbers_symbols(self, book_removed_bp):
        """Use regex to remove all non-alphabetical characters (inc. numbers)"""

        # Copy pasted from StackOverflow
        for i in range(len(book_removed_bp)):
            book_removed_bp[i] = re.sub(r"[^a-zA-z0-9]+", ' ', book_removed_bp[i])

        # New variable to avoid confusion
        words_no_symbols = book_removed_bp
        return words_no_symbols

    def format_book(self, book_removed_bp):
        """
        Formats the text such that all words are lower case and any
        whitespace is removed.
        """
        book = self.remove_numbers_symbols(book_removed_bp)

        # Strips whitespace in text and converts to lowercase
        formatted_book = [w.strip().lower() for w in book]

        return formatted_book