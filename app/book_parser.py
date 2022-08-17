from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata

class BookParser():
    def __init__(self, book_url):
        self.book_url = book_url

    def get_book_parser(self):
        """Obtains the html location and soupifies it."""
        # Read contents of URL of the book
        url = urlopen(self.book_url).read()
        soup = BeautifulSoup(url, features='html.parser')

        # Note: The brackets originally had "|" rather than " "
        book_contents = soup.get_text(" ", strip=True)
        return book_contents

    def get_book_list(self):
        """Turns the soup into a Unicode string and then into a list."""
        book_contents = self.get_book_parser()
        # NFKD deals with the spacing between characters
        normalise_soup = unicodedata.normalize('NFKD', book_contents).encode('ascii', 'ignore')
        soup_string = str(normalise_soup)

        # Turns the string into list of individual words + characters. 
        raw_book_list = soup_string.split()
        return raw_book_list