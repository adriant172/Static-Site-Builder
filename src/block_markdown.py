from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code =  "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    # blocks =  markdown.split("\n\n")
    # clean_blocks = []
    # for block in blocks:
    #     if block == "":
    #         continue
    #     block = block.strip()
    #     clean_blocks.append(block)
    # return clean_blocks
    blocks =  markdown.split("\n\n")
    clean_blocks = []
    for block in blocks:
        if block != "":
            clean_block = block.strip()
            lines = clean_block.split("\n")
            for i in range(len(lines)):
                lines[i] = lines[i].strip()
            clean_block = "\n".join(lines)
            if clean_block == "":
                continue
            clean_blocks.append(clean_block)
    return clean_blocks

def block_to_block_type(block):
    """function that converts strings of markdown 
    blocks and returns the type"""
    if block[0] == "#" and block[6] != "#":
        return block_type_heading
    if block[0:3] == "```" and block[-3:] == "```":
        return block_type_code
    lines = block.split("\n")
    line_count = len(lines)
    quote_counter = 0
    unordered_list_counter = 0
    ordered_list_counter = 1
    for line in lines:
        if line[0] == ">":
            quote_counter += 1
            continue
        if line[0] == "*" or line[0] == "-":
            unordered_list_counter += 1
            continue
        if line[0] == str(ordered_list_counter) and line[1] == ".":
            ordered_list_counter += 1
    if quote_counter == line_count:
        return block_type_quote
    if unordered_list_counter == line_count:
        return block_type_unordered_list
    if (ordered_list_counter - 1) == line_count:
        return block_type_ordered_list
    return block_type_paragraph

def text_nodes_to_inline_nodes(textnodes):
    inline_nodes = []
    for i, node in enumerate(textnodes):
        inline_nodes.append(node.text_node_to_html_node())
    return inline_nodes

def heading_block_to_htmlnode(block):
    """Converts a markdown heading 
    block string into a htmlnode """
    header_count = 0
    for char in block:
        if char == "#":
            header_count += 1
        else:
            break
    new_text = block[header_count: ]
    tag = f"h{header_count}"
    return HTMLNode(tag ,new_text)

def code_block_to_htmlnode(block):
    """Converts a markdown code
    block string into a htmlnode"""
    new_text = block[4:-3].strip()
    text_nodes = text_to_textnodes(new_text)
    inline_nodes = text_nodes_to_inline_nodes(text_nodes)
    return ParentNode("pre",[LeafNode("code",inline_nodes)])

def quote_block_to_htmlnode(block):
    """Converts a markdown quote
    block string into a htmlnode"""
    lines = block.split("\n")
    for i, line in enumerate(lines):
        lines[i] = line[1:]
    new_block = "\n".join(lines)
    text_nodes = text_to_textnodes(new_block)
    inline_nodes = text_nodes_to_inline_nodes(text_nodes)
    return ParentNode("blockquote", inline_nodes)

def ul_block_to_htmlnode(block):
    """Converts a markdown unordered list
    block string into a htmlnode"""
    list_nodes = []
    lines = block.split("\n")
    for i, line in enumerate(lines):
        text_nodes = text_to_textnodes(line[1:])
        inline_nodes = text_nodes_to_inline_nodes(text_nodes)
        list_nodes.append(ParentNode("li", inline_nodes))
    return ParentNode("ul",list_nodes)

def ol_block_to_htmlnode(block):
    """Converts a markdown unordered list
    block string into a htmlnode"""
    list_nodes = []
    lines = block.split("\n")
    for i, line in enumerate(lines):
        text_nodes = text_to_textnodes(line[2:].strip())
        inline_nodes = text_nodes_to_inline_nodes(text_nodes)
        list_nodes.append(ParentNode("li", inline_nodes))
    return ParentNode("ol",list_nodes)

def paragraph_block_to_htmlnode(block):
    text_nodes = text_to_textnodes(block)
    inline_nodes = text_nodes_to_inline_nodes(text_nodes)
    return ParentNode("p", inline_nodes)

def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    all_nodes = []
    for block in blocks:
        type_result  = block_to_block_type(block)
        if block_type_heading == type_result:
            all_nodes.append(heading_block_to_htmlnode(block))
        if block_type_code == type_result:
            all_nodes.append(code_block_to_htmlnode(block))
        if block_type_quote == type_result:
            all_nodes.append(quote_block_to_htmlnode(block))
        if block_type_unordered_list == type_result:
            all_nodes.append(ul_block_to_htmlnode(block))
        if block_type_ordered_list == type_result:
            all_nodes.append(ol_block_to_htmlnode(block))
        else:
            all_nodes.append(paragraph_block_to_htmlnode(block))
    return ParentNode("div", all_nodes)




# print(heading_block_to_htmlnode("### This is a Heading"))

test_code_block = "```\nThis is lines of code\nThis is a test\n testing 123\n```"
test_quote_block = ">This is a test\n>Testing123\n>This is another test\n>To be or not to be"
test_ul_block = "-This is a test\n-Testing123\n-This is another test\n-To be or not to be\n-one more good measure"
test_ol_block = "1. This is a test\n2. Testing123\n3. This is another test\n4. To be or not to be\n5. one more good measure"
# print(code_block_to_htmlnode(test_code_block))
# print(quote_block_to_htmlnode(test_quote_block))
test_markdown = """### Headers

Markdown supports two styles of headers, [Setext] [1] and [atx] [2].

Optionally, you may "close" atx-style headers. This is purely
cosmetic -- you can use this if you think it looks better. The
closing hashes don't even need to match the number of hashes
used to open the header. (The number of opening hashes
determines the header level.)


### Blockquotes

Markdown uses email-style `>` characters for blockquoting. If you're
familiar with quoting passages of text in an email message, then you
know how to create a blockquote in Markdown. It looks best if you hard
wrap the text and put a `>` before every line:

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

```
This is a block of code text
This is another test 
Onemore
```
"""

print(markdown_to_htmlnode(test_markdown))
