import pytest

from app.boilerplate_remover import BoilerplateRemover
class TestBoilerplateRemover:

    def test_get_boilerplate_indices(self):
        # Where no '***' appears in the text 
        # Arrange - Setting up data + creating objects
        url_book = 'https://stackoverflow.com/questions/71420952/modulenotfounderror-no-module-named-python'
        br = BoilerplateRemover(url_book)
        expected_output = []

        # Act - Do what you're testing (call methods)
        output = br.get_boilerplate_indices()

        # Assert - Asserting that it works as expected (get the desired output)
        assert output == expected_output

    def test_get_boilerplate_indices_2(self):
        
        # Where '***' does appear in the text
        url_book = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
        br = BoilerplateRemover(url_book)
        expected_output = [128, 136, 150469, 150477]

        output = br.get_boilerplate_indices()

        assert output == expected_output


    def test_remove_boilerplate(self):
        pass

