from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata
import logging
import sys

class BookParser():
    def __init__(self, book_url):
        self.book_url = book_url

    def get_book_parser(self):
        """Obtains the html location and soupifies it."""
        # Read contents of URL of the book
        try:
            url = urlopen(self.book_url).read()

        except ValueError:
            # add a logger.error here 
            print("Please supply a valid URL.")
            
        else:
            soup = BeautifulSoup(url, features='html.parser')

            # Note: The brackets originally had "|" rather than " "
            book_contents = soup.get_text(" ", strip=True)
            return book_contents

    def get_book_list(self):
        """Turns the soup into a Unicode string and then into a list."""
        try:
            book_contents = self.get_book_parser()

        except book_contents != type(str):
            print("Error: Variable 'book_contents' is not of a valid type.")
            sys.exit(1)

        else:
            # NFKD deals with the spacing between characters
            normalise_soup = unicodedata.normalize('NFKD', book_contents).encode('ascii', 'ignore')
            soup_string = str(normalise_soup)

            # Turns the string into list of individual words + characters. 
            raw_book_list = soup_string.split()
            return raw_book_list