import matplotlib.pyplot as plt

from most_common_words import MostFrequentWords


url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
bc = MostFrequentWords(url_book)
book = bc.common_words()
print(book)