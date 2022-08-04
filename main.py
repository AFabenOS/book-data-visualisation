import time
from app.data_visualiser_common_words import CommonWordChartGetter

if __name__ == '__main__':
    start_time = time.time()

    url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
    reg_book = CommonWordChartGetter(url_book)
    reg_book.get_common_word_chart()

    print("Time to run:", time.time() - start_time)

# General notes:
# Refactoring so that url_book is only passed to BookNormaliser and that subsequent passing is of the final variable list
# At present it works backwards so need to understand way to do this correctly
# Testing is very barebones on account of large lists being produced at every step - generate a smaller list that has the criteria?