import time
import logging
import logging.config

from app.data_visualiser_common_words import CommonWordChartGetter
from app.most_common_words import MostFrequentWords
from app.book_cleaner import BookCleaner
from app.boilerplate_remover import BoilerplateRemover
from app.book_parser import BookParser


if __name__ == '__main__':
    start_time = time.time()
    logging.basicConfig(filename='book.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.info("Starting process...")
    logging.info("Obtaining the HTML document and passing it through BeautifulSoup")

    book_url = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
    bp = BookParser(book_url)
    raw_book_list = bp.get_book_list()

    logging.info("Removing the boilerplate text from the book.")
    br = BoilerplateRemover()
    book_removed_bp = br.remove_boilerplate(raw_book_list)

    logging.info("Removing non-alphanumeric characters from the book.")
    bc = BookCleaner()
    formatted_book = bc.format_book(book_removed_bp)

    logging.info("Retrieving the most frequently occurring words from the book.")
    mfw = MostFrequentWords()
    frequent_words = mfw.get_frequent_words(formatted_book)

    logging.info("Producing a chart of the most frequent words.")
    reg_book = CommonWordChartGetter(frequent_words)
    reg_book.get_common_word_chart()

    logging.info("Program finished. Time to run:", time.time() - start_time)