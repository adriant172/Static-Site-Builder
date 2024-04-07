from htmlnode import HTMLNode, LeafNode, ParentNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code =  "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
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
    if block[0:2] == "```" and block[-1:-4] == "```":
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
        if int(line[0]) == ordered_list_counter and line[1] == ".":
            ordered_list_counter += 1
    if quote_counter == line_count:
        return block_type_quote
    if unordered_list_counter == line_count:
        return block_type_unordered_list
    if (ordered_list_counter - 1) == line_count:
        return block_type_ordered_list
    return block_type_paragraph

def heading_block_to_htmlnode(block):
    """Converts a markdown heading 
    block string into a htmlnode """
    header_count = 0
    for char in block:
        if char == "#":
            header_count += 1
        else:
            break
    tag = f"h{header_count}"
    return HTMLNode(tag ,block)

def code_block_to_htmlnode(block):
    return ParentNode("pre"[LeafNode("code",block)])

    
        