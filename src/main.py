from textnode import TextNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_links
from htmlnode import HTMLNode

def main():
    test_node =  TextNode(
        '''This is text with an [link 1](https://testing.com) and another [link 2](https://further-testing.com)''', "text"
    )

    result = split_nodes_links([test_node])
    print(result)


main()