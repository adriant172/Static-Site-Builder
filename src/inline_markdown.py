""" Import Textnode class """
from textnode import TextNode
import re 


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
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        lines = node.text.split(f"![{images[0][0]}]({images[0][1]})", 1)
        for i, img_tuple in enumerate(images):
            new_nodes.append(TextNode(lines[0], "text"))
            new_nodes.append(TextNode(images[i][0], "image", images[i][1]))
            if i == len(images) - 1:
                break
            lines = lines[1].split(f"![{images[i + 1][0]}]({images[i + 1][1]})", 1)
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        lines = node.text.split(f"[{links[0][0]}]({links[0][1]})", 1)
        for i, link_tuple in enumerate(links):
            new_nodes.append(TextNode(lines[0], "text"))
            new_nodes.append(TextNode(links[i][0], "link", links[i][1]))
            if i == len(links) - 1:
                break
            lines = lines[1].split(f"[{links[i + 1][0]}]({links[i + 1][1]})", 1)
    return new_nodes