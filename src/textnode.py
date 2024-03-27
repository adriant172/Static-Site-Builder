from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        if (
            (self.text == other_node.text)
            and (self.text_type == other_node.text_type)
            and (self.url == other_node.url)
        ):
            return True
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    def text_node_to_html_node(self):
        text_types =  ("text","bold","italic","code","link","image",)
        if self.text_type not in text_types:
            raise TypeError("Invalid text type.")
        match self.text_type:
            case "text":
                return LeafNode(None, self.text)
            case "bold":
                return LeafNode("b", self.text)
            case "italic":
                return LeafNode("i", self.text)
            case "code":
                return LeafNode("code", self.text)
            case "link":
                return LeafNode("a", self.text,{"href": self.url })
            case "image":
                return LeafNode("img", "", {
                    "src": self.url,
                    "alt": self.text
                })
