import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, block_type_code, block_type_heading, block_type_ordered_list, block_type_paragraph,block_type_quote, block_type_unordered_list

class TestMarkdownToBlocks(unittest.TestCase):
    """This is to test the markdown to blocks function"""
    def test_simple_block_test1(self):
        """Simple test for 3 blocks of markdown text"""
        markdown_file = """This is **bolded** paragraph

                        This is another paragraph with *italic* text and `code` here
                        This is the same paragraph on a new line

                        * This is a list
                        * with items
                        """
        blocks = markdown_to_blocks(markdown_file)
        self.assertEqual(
            blocks,
            [
                'This is **bolded** paragraph',
                'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
                '* This is a list\n* with items'
            ]
        )
    def test_simple_block_test2(self):
        """Simple test for 3 blocks of markdown text with multiple newlines in between them"""
        markdown_file = """This is **bolded** paragraph
        



                        This is another paragraph with *italic* text and `code` here
                        This is the same paragraph on a new line

                        






                        * This is a list
                        * with items
                        """
        blocks = markdown_to_blocks(markdown_file)
        self.assertEqual(
            blocks,
            [
                'This is **bolded** paragraph',
                'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
                '* This is a list\n* with items'
            ]
        )

class TestBlock_To_Block_Type(unittest.TestCase):
    """This is a test for the function that 
    converts strings of markdown blocks 
    and returns the type"""
    def test_block_to_block_ordered_list(self):
        """Test for unordered list block"""
        test_block = "1.TEST\n2.Thisis\n3.AnotherTest"
        result = block_to_block_type(test_block)
        self.assertEqual(
            result,
            block_type_ordered_list

        )
    def test_block_to_block_code(self):
        test_block = "```\nThis is lines of code\nThis is a test\n testing 123\n```"
        result = block_to_block_type(test_block)
        self.assertEqual(
            result,
            block_type_code
        )



if __name__ == "__main__":
    unittest.main()

