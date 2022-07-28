import time
from app.data_visualiser_common_words import CommonWordChartGetter

if __name__ == '__main__':
    start_time = time.time()


    url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
    reg_book = CommonWordChartGetter(url_book)
    reg_book.get_common_word_chart()

    print("Time to run:", time.time() - start_time)


