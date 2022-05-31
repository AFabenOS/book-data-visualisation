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
    return book_contents

def normalise_book(book_contents):
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
    # The commented-out code here highlights what the comprehension is doing.
    # indices = []
    # for i, s in enumerate(words):
    #     if elem in s:
    #         indices.append(i)
    return indices

def remove_boilerplate(indices, words):
    # Store index values of desired slices in variables:
    index_asterisk_1 = indices[1]
    index_asterisk_2 = indices[2]

    # Use these variables as index values to slice list and remove boilerplate
    del(words[index_asterisk_2:])
    del(words[:index_asterisk_1 + 1])
    print("No boilerplate length:", len(words))
    # with open('removeboilerplate.txt', 'w') as f:
        # f.write(str(words))
    words_no_bp = words    
    return words_no_bp

def remove_numbers_symbols(words_no_bp):
    # Use regex to remove all non-alphabetical characters (inc. numbers)
    # Copy pasted from StackOverflow
    for i in range(len(words_no_bp)):
        words_no_bp[i] = re.sub(r"[^a-zA-z]+", ' ', words_no_bp[i])
        words_no_bp[i] = re.sub(r'[0-9]+', ' ', words_no_bp[i])

    # with open('removenumberssymbols.txt', 'w') as f:
    #     f.write(str(words))
    print("New length:", len(words_no_bp))
    # New variable to avoid confusion
    words_no_symbols = words_no_bp
    return words_no_symbols

def lower_strip_clean(words_no_symbols):
    # Strips whitespace in text and converts to lowercase
    lc_words = []
    for w in words_no_symbols:
        lc_words.append(w.strip().lower())
    return lc_words

# This is the final function and where all other functions should be called    
def sort_alphabetical(lc_words):
    # Sorting occurs here
    lc_words.sort()
    alphabetical_order = lc_words
    return alphabetical_order

def parsed_text(url_book):
    book_contents = get_book_parser(url_book) #words return here
    words = normalise_book(book_contents)
    index_values = get_boilerplate_indices(words)
    remove_bp = remove_boilerplate(index_values, words) #words_no_bp returns here
    remove_num_sym = remove_numbers_symbols(remove_bp) #words_no_symbols returns here
    final_words = lower_strip_clean(remove_num_sym)
    sorted_words = sort_alphabetical(final_words)
    
    # Rename variable for clarity, not necessary
    clean_text = sorted_words
    print(clean_text)
    return clean_text

if __name__ == '__main__':
    url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm' 
    parsed_text(url_book)   


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