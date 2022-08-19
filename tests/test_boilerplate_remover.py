import pytest

from app.boilerplate_remover import BoilerplateRemover
from app.book_parser import BookParser
# (book url = "https://www.gutenberg.org/files/345/345-h/345-h.htm")
class TestBoilerplateRemover():

    @pytest.mark.parametrize(
        # Input,     Output
        "test_indice_position_list, expected_output",
        [
            (['a', 'polonium', 'ice', '**', '100', '//'], []), # No Boilerplate
            (['***', 'position', 'monkey', '***', '***', '2', '***'], [0, 3, 4, 6]) # Has Boilerplate
        ],
    )
    def test_get_boilerplate_indices(self, test_indice_position_list, expected_output):

        # Arrange - Setting up data + creating objects
        br = BoilerplateRemover()

        # Act - Do what you're testing (call methods)
        output = br.get_boilerplate_indices(test_indice_position_list)

        # Assert - Asserting that it works as expected (get the desired output)
        assert output == expected_output