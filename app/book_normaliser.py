from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata
import logging

logging.info("")

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
        """Turns the soup into a Unicode string and then into a list."""
        book_contents = self.get_book_parser()
        # NFKD deals with the spacing between characters
        normalize_soup = unicodedata.normalize('NFKD', book_contents).encode('ascii', 'ignore')
        soup_string = str(normalize_soup)

        # Turns the string into list of individual words + characters. 
        words = soup_string.split()
        return words


# Test please ignore

# url_book = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
# bc = BookNormaliser(url_book)
# print(bc.get_normalised_book())