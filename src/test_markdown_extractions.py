import unittest
from markdown_extractions import extract_markdown_images, extract_markdown_links


class TestExtractMDImagesandLinks(unittest.TestCase):
    """ This will test the extract_markdown_images function"""
    def test_images1(self):
        """First test"""
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        results = extract_markdown_images(text)
        self.assertEqual(
            results,
            [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        )
    def test_images2(self):
        """First test"""
        text = "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and [another](https://i.imgur.com/dfsdkjfd.png)"
        with self.assertRaises(Exception):
            extract_markdown_images(text)
    
    def test_links1(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        results = extract_markdown_links(text)
        self.assertEqual(
            results,
            [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        )


if __name__ == "__main__":
    unittest.main()