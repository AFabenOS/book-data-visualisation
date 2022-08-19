import pytest

from app.book_parser import BookParser

# What to test for
# Test that a valid HTML URL goes into the function
# Test that a string is returned from get_book_parser()



# book_url = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'

# class TestBookParser:

#     @pytest.mark.parametrize(
#         "test_url", "expected_output",
#         [
#             (type(book_url), type(expected_output)),
#         ],
#     )
#     def test_get_book_parser(self, test_url, expected_output):
#         # Arrange
#         #book_url = 'https://www.gutenberg.org/files/64317/64317-h/64317-h.htm'
#         bp = BookParser()


#         # Act
#         output = type(bp.get_book_parser(book_url))


#         # Assert
#         assert output == expected_output  