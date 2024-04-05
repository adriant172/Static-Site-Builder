import unittest
from block_markdown import markdown_to_blocks

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


if __name__ == "__main__":
    unittest.main()
