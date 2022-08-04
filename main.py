import time
from app.data_visualiser_common_words import CommonWordChartGetter
from app.most_common_words import MostFrequentWords
from app.book_cleaner import BookCleaner
from app.boilerplate_remover import BoilerplateRemover
from app.book_normaliser import BookNormaliser

if __name__ == '__main__':
    start_time = time.time()

    url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'

    nb = BookNormaliser(url_book)
    norm_book = nb.get_normalised_book()

    br = BoilerplateRemover()
    clean_book = br.remove_boilerplate(norm_book)

# General notes:
# Refactoring so that url_book is only passed to BookNormaliser and that subsequent passing is of the final variable list
# At present it works backwards so need to understand way to do this correctly
# Testing is very barebones on account of large lists being produced at every step - generate a smaller list that has the criteria?
