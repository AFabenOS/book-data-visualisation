import pytest

from app.book_normaliser import BookNormaliser

def test_get_book_parser(self):
    #Arrange
    url_book = 'https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python'
    bn = BookNormaliser(url_book)
    expected_output = []

    #Act
    bn.get_book_parser()

    #Assert


def test_get_normalised_book(self):
    url_book = 'https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python'
    bn = BookNormaliser(url_book)
    expected_output = []

    bn.get_book_parser()

    