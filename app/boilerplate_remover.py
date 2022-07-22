try:
    from app.book_normaliser import BookNormaliser
except ModuleNotFoundError:
    from book_normaliser import BookNormaliser
    
class BoilerplateRemover():
    def __init__(self, url_book):
        # Create an instance of BookNormaliser within BoilerplateRemover
        # So that variable words is accessible in this class
        self.normalised_book = BookNormaliser(url_book)
        
    def get_boilerplate_indices(self):
        """
        Returns the indices value of the boilerplate text which is before
        the second and after the third appearance of '***' in the text.
        """
        elem = "***"
        indices = [i for i, s in enumerate(self.normalised_book.get_normalised_book()) if elem in s]
        return indices
        # The commented-out code here highlights what the comprehension is doing.
        # indices = []
        # for i, s in enumerate(words):
        #     if elem in s:
        #         indices.append(i)

    def remove_boilerplate(self):
        """Removes the boilerplate text from variable words using the indices 
        values obtained from get_boilerplate_indices"""
        # Assign the function calls as variables
        bp_index = self.get_boilerplate_indices()
        book_with_bp = self.normalised_book.get_normalised_book()

        # Store index values of desired slices in variables:
        index_asterisk_1 = bp_index[1]
        index_asterisk_2 = bp_index[2]
        print("ia1", index_asterisk_1, "ia2", index_asterisk_2)

        # Delete all items before and after the specific index values
        # Prove by showing length of book has decreased
        print("Book with boilerplate length:", len(book_with_bp))

        # The second index deletion happens before the first since the location
        # of elem would be altered.
        del(book_with_bp[index_asterisk_2:])
        del(book_with_bp[:index_asterisk_1])
        print("Removed boilerplate length:", len(book_with_bp))

        # Transform variable name so it makes sense
        book_no_bp = book_with_bp
        return book_no_bp