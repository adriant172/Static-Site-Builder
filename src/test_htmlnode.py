import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html1(self):
        node = HTMLNode("p", "This is a test node")
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html2(self):
        node = HTMLNode(
            "a",
            "HyperLink",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')


class TestLeafNode(unittest.TestCase):
    def test_to_html1(self):
        node = LeafNode("p", "This a leaf node test.")
        result = node.to_html()
        self.assertEqual(result, "<p>This a leaf node test.</p>")

    def test_to_html2(self):
        node = LeafNode(
            tag="a", value="Click me!", props={"href": "https://www.google.com"}
        )
        result = node.to_html()
        self.assertEqual(result, '<a href="https://www.google.com">Click me!</a>')


class TestParentNode(unittest.TestCase):
    def test_to_html1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        result = node.to_html()
        self.assertEqual(
            result, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html2(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "li",
                    [
                        ParentNode(
                            "li",
                            [
                                LeafNode("ul", "Text1"),
                                LeafNode("ul", "Text2"),
                                LeafNode("ul", "Text3"),
                                LeafNode("ul", "Text4"),
                            ],
                        ),
                        LeafNode("ul", "Text1"),
                        LeafNode("ul", "Text2"),
                        LeafNode("ul", "Text3"),
                        LeafNode("ul", "Text4"),
                    ],
                ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        result = node.to_html()
        self.assertEqual(
            result,
            "<p><li><li><ul>Text1</ul><ul>Text2</ul><ul>Text3</ul><ul>Text4</ul></li><ul>Text1</ul><ul>Text2</ul><ul>Text3</ul><ul>Text4</ul></li>Normal text<i>italic text</i>Normal text</p>",
        )
