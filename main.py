import time
import logging

from app.data_visualiser_common_words import CommonWordChartGetter
from app.most_common_words import MostFrequentWords
from app.book_cleaner import BookCleaner
from app.boilerplate_remover import BoilerplateRemover
from app.book_parser import BookParser

if __name__ == '__main__':
    start_time = time.time()
    # logging.basicConfig(filename="logs.txt", level=logging.INFO)
    # logging.info("Starting process...")

    book_url = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
    bp = BookParser(book_url)
    raw_book_list = bp.get_book_list()

    br = BoilerplateRemover()
    book_removed_bp = br.remove_boilerplate(raw_book_list)

    bc = BookCleaner()
    formatted_book = bc.format_book(book_removed_bp)

    mfw = MostFrequentWords()
    frequent_words = mfw.get_frequent_words(formatted_book)

    reg_book = CommonWordChartGetter(frequent_words)
    reg_book.get_common_word_chart()

    print("Time to run:", time.time() - start_time)
