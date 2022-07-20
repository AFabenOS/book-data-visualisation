import re
from boilerplate_remover import BoilerplateRemover

class BookCleaner():
    def __init__(self, url_book):
        self.book = BoilerplateRemover(url_book)
        
    def remove_numbers_symbols(self):
        """Use regex to remove all non-alphabetical characters (inc. numbers)"""
        clean_book = self.book.remove_boilerplate()
        # Copy pasted from StackOverflow
        for i in range(len(clean_book)):
            clean_book[i] = re.sub(r"[^a-zA-z]+", ' ', clean_book[i])
            clean_book[i] = re.sub(r'[0-9]+', ' ', clean_book[i])

        # with open('removenumberssymbols.txt', 'w') as f:
        #     f.write(str(words))

        # New variable to avoid confusion
        words_no_symbols = clean_book
        return words_no_symbols

    def format_book(self):
        """
        Formats the text such that all words are lower case and any
        whitespace is removed.
        """
        book = self.remove_numbers_symbols()

        # Strips whitespace in text and converts to lowercase
        formatted_book = []
        for w in book:
            formatted_book.append(w.strip().lower())

        return formatted_book
    
    def sort_alphabetical(self):
        """Sorts the book alphabetically."""
        book = self.format_book()
        book.sort()
        alphabetical_order = book

        return alphabetical_order
