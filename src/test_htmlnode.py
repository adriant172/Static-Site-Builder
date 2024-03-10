import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html1(self):
        node = HTMLNode("p", "This is a test node")
        result = node.props_to_html()
        self.assertEqual(result, None)
        
    def test_props_to_html2(self):
        node = HTMLNode("a", "HyperLink", None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, 'href="https://www.google.com" target="_blank"')
