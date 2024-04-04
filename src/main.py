from textnode import TextNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_links, text_to_textnodes
from htmlnode import HTMLNode

def main():
    test_text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    result = text_to_textnodes(test_text)
    print(result)


main()
