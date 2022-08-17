import pytest

from app.boilerplate_remover import BoilerplateRemover
from app.book_parser import BookParser

class TestBoilerplateRemover:

    @pytest.mark.parametrize(
        # Input,     Output
        "book_url, expected_output",
        [
            ("https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python", []), # No Boilerplate
            ("https://www.gutenberg.org/files/345/345-h/345-h.htm", [128, 136, 150469, 150477]), # Has Boilerplate
            # pytest.param("6*9", 42, marks=pytest.mark.xfail)
        ],
    )
    def test_get_boilerplate_indices(self, book_url, expected_output):


        # Arrange - Setting up data + creating objects
        br = BoilerplateRemover(book_url)

        # Act - Do what you're testing (call methods)
        output = br.get_boilerplate_indices()

        # Assert - Asserting that it works as expected (get the desired output)
        assert output == expected_output
    
    @pytest.mark.parametrize(
        # Input,      Output
        "url_book, expected_output",
        [
            ()
            ("https://www.gutenberg.org/files/345/345-h/345-h.htm", )

    # def test_remove_boilerplate(self):
    #     book_url = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
    #     br = BoilerplateRemover(book_url)

    #     nb = BookNormaliser(book_url)
    #     nb.get_normalised_book()

    #     expected_output = []

    #     output = br.get_boilerplate_indices()

    #     assert output == expected_output
