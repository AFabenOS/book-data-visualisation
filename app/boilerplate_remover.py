try:
    from app.book_parser import BookParser
except ModuleNotFoundError:
    from book_parser import BookParser

    
class BoilerplateRemover():

    def get_boilerplate_indices(self, raw_book_list):
        """
        Returns the indices where the boilerplate text occurs which is denoted with '***' in the text.
        """

        elem = "***"
        indices = [i for i, s in enumerate(raw_book_list) if elem in s]
        return indices
        
        # The commented-out code here highlights what the comprehension is doing.
        # indices = []
        # for i, s in enumerate(words):
        #     if elem in s:
        #         indices.append(i)

    def remove_boilerplate(self, raw_book_list):
        """
        Removes the boilerplate text from variable words using the indices 
        values obtained from get_boilerplate_indices()
        """

        # Assign the function calls as variables
        bp_index = self.get_boilerplate_indices(raw_book_list)
        # norm book

        # Store index values of desired slices in variables:
        index_asterisk_1 = bp_index[1]
        index_asterisk_2 = bp_index[2]
        print("ia1", index_asterisk_1, "ia2", index_asterisk_2)

        # Delete all items before and after the specific index values
        # Prove by showing length of book has decreased
        print("Book with boilerplate length:", len(raw_book_list))

        # The second index deletion happens before the first since the location
        # of elem would be altered.
        del(raw_book_list[index_asterisk_2:])
        del(raw_book_list[:index_asterisk_1])
        print("Removed boilerplate length:", len(raw_book_list))

        # Transform variable name so it makes sense
        return raw_book_list