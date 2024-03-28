import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_links

class TestSplitNodes(unittest.TestCase):
    """Test the split_nodes_delimiter function"""
    def test_1(self):
        """First test"""
        test_node = TextNode("This is text with a `code block` word.", "code")
        result = split_nodes_delimiter([test_node], "`","code")
        self.assertEqual(
            result,
            [
                TextNode("This is text with a ", "text", None),
                TextNode("code block", "code", None),
                TextNode(" word.", "text", None),
            ]

        )
    def test_2(self):
        test_node = TextNode("This is text with a `code block word.", "code")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([test_node], "`","code")
    
    def test_3(self):
        test_node = TextNode("This is text with a `code block` word.", "code")
        htmlnode = HTMLNode(None, None, None,None)
        result = split_nodes_delimiter([htmlnode,test_node], "`","code")
       
        self.assertEqual(
            result,
            [
                htmlnode,
                TextNode("This is text with a ", "text", None),
                TextNode("code block", "code", None),
                TextNode(" word.", "text", None)
            ]

        )
    def test_4(self):
        test_node = TextNode("This is text with a **bolded word** and **another**", "text")
        result = split_nodes_delimiter([test_node], "**", "b")

        self.assertEqual(
            result, [
                TextNode("This is text with a ", "text", None),
                TextNode("bolded word", "b", None),
                TextNode(" and ", "text", None),
                TextNode("another", "b", None)
            ]
            
        )

class TestExtractMDImagesandLinks(unittest.TestCase):
    """This will test the extract_markdown_images function"""
    def test_images1(self):
        """First test"""
        text = '''This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)
         and ![another](https://i.imgur.com/dfsdkjfd.png)'''
        results = extract_markdown_images(text)
        self.assertEqual(
            results,
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("another", "https://i.imgur.com/dfsdkjfd.png"),
            ],
        )

    # def test_images2(self):
    #     """Testing the error catching functionality"""
    #     text ='''This is text with an [image](https://i.imgur.com/zjjcJKZ.png)
    #      and [another](https://i.imgur.com/dfsdkjfd.png)'''
    #     with self.assertRaises(Exception):
    #         extract_markdown_images(text)

    def test_links1(self):
        """First test for extracting links"""
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        results = extract_markdown_links(text)
        self.assertEqual(
            results,
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another"),
            ],
        )

class TestSplitNodesImage(unittest.TestCase):
    """ This is to test the split_nodes_images function"""
    test_node =  TextNode(
        '''This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)''',
        "text",)
    test_node2 =  TextNode(
        '''This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and one more for good measure ![third image](https://i.imgur.com/3elNhQu.png)''',
        "text",)

    def test_split_node_images1(self):
        new_nodes = split_nodes_image([self.test_node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", "text"),
                TextNode(
                    "second image", "image", "https://i.imgur.com/3elNhQu.png"
                ),
            ]

        )
    def test_split_node_images2(self):
        new_nodes = split_nodes_image([self.test_node2])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", "text"),
                TextNode(
                    "second image", "image", "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and one more for good measure ", "text"),
                TextNode("third image", "image", "https://i.imgur.com/3elNhQu.png")
            ]

        )
    def test_split_node_multiple_images1(self):
        new_nodes = split_nodes_image([self.test_node, self.test_node2])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", "text"),
                TextNode(
                    "second image", "image", "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", "text"),
                TextNode(
                    "second image", "image", "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and one more for good measure ", "text"),
                TextNode("third image", "image", "https://i.imgur.com/3elNhQu.png")
            ]
        )

        

class TestSplitNodesLinks(unittest.TestCase):
    """ This is for testing the split_nodes_links function"""
    def test_split_nodes_links(self):
        """ First basic test """
        test_node =  TextNode(
        '''This is text with an [link 1](https://testing.com) and another [link 2](https://further-testing.com)''',
        "text",)
        new_nodes = split_nodes_links([test_node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", "text"),
                TextNode("link 1", "link", "https://testing.com"),
                TextNode(" and another ", "text"),
                TextNode(
                    "link 2", "link", "https://further-testing.com"
                ),
            ]
        )
            



if __name__ == "__main__":
    unittest.main()