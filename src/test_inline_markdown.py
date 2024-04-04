import unittest

from textnode import TextNode, text_types
from htmlnode import HTMLNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_links, text_to_textnodes

class TestSplitNodes(unittest.TestCase):
    """Test the split_nodes_delimiter function"""
    def test_1(self):
        """First test"""
        test_node = TextNode("This is text with a `code block` word.", "text")
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
        test_node = TextNode("This is text with a `code block word.", "text")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([test_node], "`","code")
    
    def test_3(self):
        test_node = TextNode("This is text with a `code block` word.", "text")
        test_node2 = TextNode("This is text with a `code block` word.", "code")
        result = split_nodes_delimiter([test_node,test_node2,], "`","code")
       
        self.assertEqual(
            result,
            [
                TextNode("This is text with a ", "text", None),
                TextNode("code block", "code", None),
                TextNode(" word.", "text", None),
                test_node2
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
        '''This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and one more for good measure ![third image](https://i.imgur.com/3elNhQu.png) and a [link 2](https://further-testing.com)''',
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
                TextNode("third image", "image", "https://i.imgur.com/3elNhQu.png"),
                TextNode(" and a [link 2](https://further-testing.com)", "text", None)
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
                TextNode("third image", "image", "https://i.imgur.com/3elNhQu.png"),
                TextNode(" and a [link 2](https://further-testing.com)", "text", None)
            ]
        )

        

class TestSplitNodesLinks(unittest.TestCase):
    """ This is for testing the split_nodes_links function"""
    def test_split_nodes_link1(self):
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
            

class TestTextToTestNodes(unittest.TestCase):
    """This is for testing the text_to_textnodes function"""
    def test_text_to_testnodes1(self):
        test_text = """This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"""
        test_nodes = text_to_textnodes(test_text)
        self.assertEqual(
            test_nodes,
            [
                TextNode("This is ", text_types["text"]),
                TextNode("text", text_types["bold"]),
                TextNode(" with an ", text_types["text"]),
                TextNode("italic", text_types["italic"]),
                TextNode(" word and a ", text_types["text"]),
                TextNode("code block", text_types["code"]),
                TextNode(" and an ", text_types["text"]),
                TextNode("image", text_types["image"], "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_types["text"]),
                TextNode("link", text_types["link"], "https://boot.dev"),
            ]

        )

if __name__ == "__main__":
    unittest.main()