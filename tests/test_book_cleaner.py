import pytest
import app

# FUTURE ANDREW LOOK UP MOCKING

from app.book_cleaner import BookCleaner
from app.boilerplate_remover import BoilerplateRemover
from app.book_normaliser import BookNormaliser

class TestBookCleaner:

    def test_remove_numbers_symbols(self):
        
        # Arrange - Setting up data + creating objects
        url_book = ''
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
