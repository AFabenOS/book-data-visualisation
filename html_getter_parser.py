from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata
import re

class BookNormaliser():
    def __init__(self, url_book):
        self.url_book = url_book

    def get_book_parser(self):
        """Obtains the html location and soupifies it."""
        # Read contents of URL of the book
        html = urlopen(self.url_book).read()
        soup = BeautifulSoup(html, features='html.parser')

        # Note: The brackets originally had "|" rather than " "
        book_contents = soup.get_text(" ", strip=True)
        return book_contents

    def get_normalised_book(self):
        """Turns the soup into a list of the contents."""
        book_contents = self.get_book_parser()
        # NFKD deals with the spacing between characters
        normalize_soup = unicodedata.normalize('NFKD', book_contents).encode('ascii', 'ignore')
        soup_string = str(normalize_soup)

        # Turns the string into list of individual words + characters. 
        words = soup_string.split()
        return words

class BoilerplateRemover():
    def __init__(self, url_book):
        # Create an instance of BookNormaliser within BoilerplateRemover
        # So that variable words is accessible in this class
        self.normalised_book = BookNormaliser(url_book)
        
    def get_boilerplate_indices(self):
        """
        Returns the indices value of the boilerplate text which is before
        the second and after the third appearance of '***' in the text.
        """
        elem = "***"
        indices = [i for i, s in enumerate(self.normalised_book.get_normalised_book()) if elem in s]
        return indices
        # The commented-out code here highlights what the comprehension is doing.
        # indices = []
        # for i, s in enumerate(words):
        #     if elem in s:
        #         indices.append(i)

    def remove_boilerplate(self):
        """Removes the boilerplate text from variable words using the indices 
        values obtained from get_boilerplate_indices"""
        # Assign the function calls as variables
        bp_index = self.get_boilerplate_indices()
        book_with_bp = self.normalised_book.get_normalised_book()

        # Store index values of desired slices in variables:
        index_asterisk_1 = bp_index[1]
        index_asterisk_2 = bp_index[2]
        print("ia1", index_asterisk_1, "ia2", index_asterisk_2)

        # Delete all items before and after the specific index values
        # Prove by showing length of book has decreased
        print("Book with boilerplate length:", len(book_with_bp))
        # The second index deletion happens before the first since the location
        # of elem would be altered.
        del(book_with_bp[index_asterisk_2:])
        del(book_with_bp[:index_asterisk_1])
        print("Removed boilerplate length:", len(book_with_bp))

        book_no_bp = book_with_bp
        return book_no_bp

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
        print(len(alphabetical_order))
        return alphabetical_order

# if __name__ == '__main__':
url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
reg_book = BookCleaner(url_book)
reg_book.sort_alphabetical()

# This is the final function and where all other functions should be called    

# def get_parsed_text(url_book):
#     book_contents = get_book_parser(url_book) #words return here
#     words = get_normalised_book(book_contents)
#     index_values = get_boilerplate_indices(words)
#     remove_bp = remove_boilerplate(index_values, words) #words_no_bp returns here
#     remove_num_sym = remove_numbers_symbols(remove_bp) #words_no_symbols returns here
#     final_words = lower_strip_clean(remove_num_sym)
#     sorted_words = sort_alphabetical(final_words)
    
    # # Rename variable for clarity, not necessary
    # clean_text = sorted_words
    # return clean_text



    
    # This is functional so far. Needs a function call within 
    # normalise_book() to avoid calling a bunch of methods in here
    # Alternatively, make a third method that calls in both methods
    # so that each method has a clear defined purpose

    # Then need to transfer the results of these methods from the class
    # into the next class somehow, might be a case of making a new variable
    # and passing in that variable to the next method in the class??