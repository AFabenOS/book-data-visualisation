import pytest

from app.most_common_words import MostFrequentWords

def test_get_frequent_words(self):
    #Arrange
    book_url = 'https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python'
    bn = MostFrequentWords(book_url)
    expected_output = []

    #Act
    bn.common_words()

    #Assert