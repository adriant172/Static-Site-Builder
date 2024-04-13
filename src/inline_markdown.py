""" Import Textnode class """
from textnode import TextNode, text_types
import re 


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    # text_types = ("code", "b", "i")
    for node in old_nodes:
        if node.text_type != text_types["text"]:
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



def extract_markdown_images(text):
    """Extract markdown images from a string and return a list of tuples"""
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    """Extract markdown links from a string and return a list of tuples"""
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        raw_text = node.text
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            lines = raw_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(lines) != 2:
                raise ValueError("Invalid, image is missing closing bracket")
            new_nodes.append(TextNode(lines[0], "text"))
            new_nodes.append(TextNode(image[0], "image", image[1]))
            raw_text = lines[1]
        if raw_text != "":
            new_nodes.append(TextNode(raw_text, "text"))
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        raw_text = node.text
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        lines = node.text.split(f"[{links[0][0]}]({links[0][1]})", 1)
        for link in links:
            lines = raw_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(lines) != 2:
                raise ValueError("Invalid, link is missing closing bracket")
            new_nodes.append(TextNode(lines[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            raw_text = lines[1]
        if raw_text != "":
            new_nodes.append(TextNode(raw_text, "text"))
    return new_nodes

def text_to_textnodes(text):
    """ Linking together functions together into a 
    function that can convert a raw string of markdown 
    flavored text into a list of TextNode objects"""
    old_node = TextNode(text, text_types["text"])
    new_nodes = [old_node]
    result = split_nodes_links(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(new_nodes, "**", "bold"),"*", "italic"),"`", "code")))
    return result
    # return split_nodes_links(split_nodes_image(new_nodes))
