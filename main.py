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

    # Set book_analysis_logger
    book_analysis_logger = logging.getLogger('book_analysis_logger')
    # Set formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    # Set and add handler
    handler = logging.FileHandler('book.log', mode = 'w')
    handler.setFormatter(formatter)
    # check if handler already exists
    if len(book_analysis_logger.handlers) == 1:
        book_analysis_logger.handlers.clear()
    book_analysis_logger.addHandler(handler)
    # Set and add level
    book_analysis_logger.setLevel(logging.DEBUG)

    book_analysis_logger.info("Starting process...")
    book_analysis_logger.info("Obtaining the HTML document and passing it through BeautifulSoup")

    book_url = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
    bp = BookParser(book_url)
    raw_book_list = bp.get_book_list()

    book_analysis_logger.info("Removing the boilerplate text from the book.")
    br = BoilerplateRemover()
    book_removed_bp = br.remove_boilerplate(raw_book_list)

    book_analysis_logger.info("Removing non-alphanumeric characters from the book.")
    bc = BookCleaner()
    formatted_book = bc.format_book(book_removed_bp)

    book_analysis_logger.info("Retrieving the most frequently occurring words from the book.")
    mfw = MostFrequentWords()
    frequent_words = mfw.get_frequent_words(formatted_book)

    book_analysis_logger.info("Producing a chart of the most frequent words.")
    reg_book = CommonWordChartGetter(frequent_words)
    reg_book.get_common_word_chart()

    end_time = time.time()
    time_to_run = end_time - start_time
    book_analysis_logger.info(f"Program finished. Time to run: {str(time_to_run)}")