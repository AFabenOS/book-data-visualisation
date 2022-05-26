from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata
import re

def get_book_parser(book):
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

def get_boilerplate_indices(words):

    print("Original length:", len(words))
    elem = "***"
    # Stolen from SO (don't understand list comprehensions yet):
    indices = [i for i, s in enumerate(words) if elem in s]
    return indices

def remove_boilerplate(index_values, words):

    # Store index values of desired slices in variables:
    index_asterisk_1 = index_values[1]
    index_asterisk_2 = index_values[2]

    # Use these variables as index values to slice list and remove boilerplate
    del(words[index_asterisk_2:])
    del(words[:index_asterisk_1 + 1])
    print("No boilerplate length:", len(words))
    # with open('removeboilerplate.txt', 'w') as f:
        # f.write(str(words))
    words_no_bp = words    
    return words_no_bp

def remove_numbers_symbols(remove_bp, words):
    # Use regex to remove all non-alphabetical characters (inc. numbers)
    # Copy pasted from StackOverflow
    for i in range(len(words)):
        words[i] = re.sub(r"[^a-zA-z]+", ' ', words[i])
        words[i] = re.sub(r'[0-9]+', ' ', words[i])
    # with open('removenumberssymbols.txt', 'w') as f:
    #     f.write(str(words))
    print("New length:", len(words))
    return words

def clean_text(remove_num_sym, words):
    # Strips whitespace in text and converts to lowercase
    lc_words = []
    for w in words:
        lc_words.append(w.strip().lower())
    return lc_words

# This is the final function and where all other functions should be called    
def sort_alphabetical(book):
    # In order to sort the words, need to get every other function in here
    words = get_book_parser(book)
    # NEED TO CHANGE PARAMETER NAMES, IT'S USING THE SAME PARAMETER AND NOT CARRYING FORWARD
    index_values = get_boilerplate_indices(words)

    remove_bp = remove_boilerplate(index_values, words)

    remove_num_sym = remove_numbers_symbols(remove_bp, words)

    final_clean = clean_text(remove_num_sym, words)

    words = clean_text(final_clean, words)
    words.sort()
    print(words)
    print(len(words))
    return words

if __name__ == '__main__':

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