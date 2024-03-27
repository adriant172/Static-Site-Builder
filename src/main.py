from textnode import TextNode
from split_nodes import split_nodes_delimiter
from htmlnode import HTMLNode

def main():
    test_node = TextNode("This is text with a `code block` word.", "code")
    # htmlnode = test_node.text_node_to_html_node()
    # print(htmlnode)
    test_node = TextNode("This is text with a **bolded word** and **another**", "text")
    result = split_nodes_delimiter([test_node], "**", "b")
    # result = split_nodes_delimiter([test_node], "`","code")
    print(result)

main()