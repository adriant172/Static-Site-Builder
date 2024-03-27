import unittest

from textnode import TextNode
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    """ TestNode test cases"""
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node,node2)
    def test_eq3(self):
        node = TextNode("This is a text node", "italic", "www.test.com")
        node2 = TextNode("This is a text node", "italic", "www.test.com")
        self.assertEqual(node,node2)
    def test_eq4(self):
        node = TextNode("This is a text node", "italic", None)
        node2 = TextNode("This is a text node", "italic", None)
        self.assertEqual(node,node2)
    def test_textnode_to_htmlnode(self):
        textnode = TextNode("This is a text node", "link", "https://www.boot.dev")
        htmlnode = textnode.text_node_to_html_node()
        self.assertEqual(str(htmlnode), "LeafNode(a, This is a text node, None, {'href': 'https://www.boot.dev'})")

if __name__ == "__main__":
    unittest.main()
