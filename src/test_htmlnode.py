import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html1(self):
        node = HTMLNode("p", "This is a test node")
        result = node.props_to_html()
        self.assertEqual(result, "")
        
    def test_props_to_html2(self):
        node = HTMLNode("a", "HyperLink", None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_to_html1(self):
        node = LeafNode("This a leaf node test.", "p")
        result = node.to_html()
        self.assertEqual(result, "<p>This a leaf node test.</p>")
    def test_to_html2(self):
        node = LeafNode(value="Click me!", tag="a", props={"href": "https://www.google.com"})
        result = node.to_html()
        self.assertEqual(result, '<a href="https://www.google.com">Click me!</a>')
