import pytest

from app.most_common_words import MostFrequentWords

def test_common_words(self):
    #Arrange
    url_book = 'https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python'
    bn = MostFrequentWords(url_book)
    expected_output = []

    #Act
    bn.common_words()

    #Assert


def test_common_words_2(self):
    url_book = 'https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python'
    bn = MostFrequentWords(url_book)
    expected_output = []

    bn.common_words()