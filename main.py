from app.book_cleaner import BookCleaner
from app.boilerplate_remover import BoilerplateRemover

if __name__ == '__main__':
    url_book = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
    reg_book = BookCleaner(url_book)
    reg_book.sort_alphabetical()

