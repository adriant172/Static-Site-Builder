""" Import Textnode class """
from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    text_types = ("code", "b", "i")
    if text_type not in text_types:
        raise ValueError("Incorrect text type. Use either code, b or i.")
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue
        words = node.text.split(delimiter)
        if len(words) % 2 == 0:
            raise ValueError("Closing delimiter is missing")
        for i, string in enumerate(words):
            if string == "":
                continue
            if i % 2 == 1: 
                new_nodes.append(TextNode(string, text_type))
            else:
                new_nodes.append(TextNode(string, "text"))
    return new_nodes