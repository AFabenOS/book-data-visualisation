import pytest

from app.book_cleaner import BookCleaner
from app.boilerplate_remover import BoilerplateRemover

class TestBookCleaner:
    
    @pytest.mark.parametrize(
        "test_list, expected_output",
        [
            (['a', 'b', 'c', 'd.', ',...'], ['a', 'b', 'c', 'd ', ' ']),
            (['a--', 'b,@', 'c#', 'd.', ',...'], ['a ', 'b ', 'c ', 'd ', ' ']),
        ],
    )
    def test_remove_nonalphanumeric(self, test_list, expected_output):  
        # Arrange
        bc = BookCleaner()

        # Act
        output = bc.remove_nonalphanumeric(test_list)
        # Assert
        assert output == expected_output
    
    # @pytest.mark.parametrize(
    #     "test_list, expected_output",
    #     [
    #         (['a ', 'b ', 'c ', 'd ', ' '], ['a', 'b', 'c', 'd', '']),
    #     ],
    # )
    # def test_format_book(self, test_list, expected_output):
    #     bc = BookCleaner

    #     remove_alphanumeric = bc.remove_nonalphanumeric()

    #     # Act
    #     output = bc.format_book(remove_alphanumeric)

    #     # Assert
    #     assert output == expected_output
