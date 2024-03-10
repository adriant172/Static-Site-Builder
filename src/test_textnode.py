import unittest

from textnode import TextNode


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
    



if __name__ == "__main__":
    unittest.main()
