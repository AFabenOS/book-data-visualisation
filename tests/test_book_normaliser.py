import pytest

from app.book_parser import BookNormaliser

def test_get_book_parser(self):
    #Arrange
    book_url = 'https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python'
    bn = BookNormaliser(book_url)
    expected_output = []

    #Act
    bn.get_book_parser()

    #Assert


def test_get_normalised_book(self):
    book_url = 'https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python'
    bn = BookNormaliser(book_url)
    expected_output = []

    bn.get_book_parser()

    