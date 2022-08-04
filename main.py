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

    bc = BookCleaner()
    book_common = bc.format_book(clean_book)

    mfw = MostFrequentWords()
    common_words = mfw.common_words(book_common)

    reg_book = CommonWordChartGetter(common_words)
    reg_book.get_common_word_chart()

    print("Time to run:", time.time() - start_time)