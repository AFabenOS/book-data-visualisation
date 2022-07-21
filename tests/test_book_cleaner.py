# FUTURE ANDREW LOOK UP MOCKING
import unittest

from app.book_cleaner import BookCleaner

class TestBookCleaner:

    def test_remove_numbers_symbols(self):  
        # Arrange - Setting up data + creating objects
        url_book = 'https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python'
        bc = BookCleaner(url_book)
        expected_output = []

        # Act - Do what you're testing (call methods)
        output = bc.remove_numbers_symbols()

        # Assert - Asserting that it works as expected (get the desired output)
        assert output == expected_output

    def test_format_book(self):
        pass

    def test_sort_alphabetical(self):
        pass