import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from split_nodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    """Test the split_nodes_delimiter function"""
    def test_1(self):
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

if __name__ == "__main__":
    unittest.main()