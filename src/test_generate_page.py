import unittest
from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):
    def test_extract_title_basic(self):
        """Basic extraction of a header when 
        it is the first line of a markdown file"""
        markdown = """# This is a header

This is a **bolded** paragraph text. 
Meant for testing. That has some *stylized* text for additional 
`testing purposes`. Hopefully this is a good test."""
        title = extract_title(markdown)
        self.assertEqual(
            title,
            "# This is a header"

        )
    def test_extract_title_basic2(self):
        """Try to extract the header when there is some text before it"""
        markdown = """ This is some text before the header

        # This is a header

This is a **bolded** paragraph text. 
Meant for testing. That has some *stylized* text for additional 
`testing purposes`. Hopefully this is a good test."""
        title = extract_title(markdown)
        self.assertEqual(
            title,
            "# This is a header"

        )


if __name__ == "__main__":
     unittest.main()
