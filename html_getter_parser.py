from itertools import count
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata
import re

def book_parser(book):
    # Read contents of URL of the book
    html = urlopen(book).read()
    soup = BeautifulSoup(html, features='html.parser')

    # Note: The brackets originally had "|" rather than " "
    book_contents = soup.get_text(" ", strip=True)

    # Turns the soup into one big string
    # NFKD deals with the spacing between characters
    normalize_soup = unicodedata.normalize('NFKD', book_contents).encode('ascii', 'ignore')
    soup_string = str(normalize_soup)

    # Turns the string into list of individual words + characters. 
    words = soup_string.split()
    return words

def remove_boilerplate(book):
    words = book_parser(book)

    print("Original length:", len(words))
    elem = "***"
    # Stolen from SO (don't understand list comprehensions yet):
    indices = [i for i, s in enumerate(words) if elem in s]
    print(indices)

    # Store index values of desired slices in variables:
    index_asterisk_1 = indices[1]
    index_asterisk_2 = indices[2]

    # Use these variables as index values to slice list and remove boilerplate
    del(words[index_asterisk_2:])
    del(words[:index_asterisk_1 + 1])
    print("No boilerplate length:", len(words))
    # with open('removeboilerplate.txt', 'w') as f:
        # f.write(str(words))
    return words

def remove_numbers_symbols(book):
    words = remove_boilerplate(book)
    # Use regex to remove all non-alphabetical characters (inc. numbers)
    # Copy pasted from StackOverflow
    for i in range(len(words)):
        words[i] = re.sub(r"[^a-zA-z]+", ' ', words[i])
        words[i] = re.sub(r'[0-9]+', ' ', words[i])
    # with open('removenumberssymbols.txt', 'w') as f:
    #     f.write(str(words))
    print("New length:", len(words))
    return words

def clean_text(book):
    # Strips whitespace in text and converts to lowercase
    words = remove_numbers_symbols(book)
    lc_words = []
    for w in words:
        lc_words.append(w.strip().lower())
    return lc_words
    
    # Converts everything to lower case, since A != a in Python

def sort_alphabetical(book):
    words = clean_text(book)
    words.sort()
    print(words)

url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm' 
sort_alphabetical(url_book)

if __name__ == '__main__':
    assert book_parser()
    
    url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm' 
    sort_alphabetical(url_book)

# Once all the functions are written, refactor accordingly, such that
# the book parameter isn't being passed to every function when it only needs to
# be done once

# class HTMLGetterAndParser():
#     """
#     Class that takes in a URL that contains text in HTML format,
#     parses and cleans it.
#     """

#     def __init__(self):
#         pass

#     def html_getter(self):
#         pass

#     def pj_text_deleter(self):
#         pass

#     def remove_numbers(self):
#         pass

#     def erroneous_cleaning(self):
#         pass

#     def remove_single_letters_not_a_i(self):
#         pass

#     def convert_lower(self):
#         pass

#     def sort_alphabetical(self):
#         pass