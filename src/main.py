from textnode import TextNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_links, text_to_textnodes
from htmlnode import HTMLNode
from copy_static import copy_dir, clear_dir

static_path = "./static"
public_path = "./public"

def main():
    clear_dir(public_path)
    copy_dir(static_path, public_path)

main()