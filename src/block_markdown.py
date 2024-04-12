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
    blocks =  markdown.split("\n\n")
    clean_blocks = []
    for block in blocks:
        if block != "":
            clean_block = block.strip()
            lines = clean_block.split("\n")
            for i, line in enumerate(lines):
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
    """This converts text nodes into html nodes that will be used to make inline nodes """
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
    new_text = block[header_count + 1: ]
    text_nodes = text_to_textnodes(new_text)
    inline_nodes = text_nodes_to_inline_nodes(text_nodes)
    tag = f"h{header_count}"
    return ParentNode(tag , inline_nodes)

def code_block_to_htmlnode(block):
    """Converts a markdown code
    block string into a htmlnode"""
    new_text = block[4:-3].strip()
    text_nodes = text_to_textnodes(new_text)
    inline_nodes = text_nodes_to_inline_nodes(text_nodes)
    return ParentNode("pre",[ParentNode("code",inline_nodes)])

def quote_block_to_htmlnode(block):
    """Converts a markdown quote
    block string into a htmlnode"""
    lines = block.split("\n")
    new_lines = []
    for i, line in enumerate(lines):
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    new_block = " ".join(new_lines)
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
    lines = block.split("\n")
    # for i , line in enumerate(lines):
    #     lines[i] = line.strip()
    new_lines = " ".join(lines)
    text_nodes = text_to_textnodes(new_lines)
    inline_nodes = text_nodes_to_inline_nodes(text_nodes)
    return ParentNode("p", inline_nodes)

def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    all_nodes = []
    for block in blocks:
        type_result  = block_to_block_type(block)
        if block_type_heading == type_result:
            all_nodes.append(heading_block_to_htmlnode(block))
        elif block_type_code == type_result:
            all_nodes.append(code_block_to_htmlnode(block))
        elif block_type_quote == type_result:
            all_nodes.append(quote_block_to_htmlnode(block))
        elif block_type_unordered_list == type_result:
            all_nodes.append(ul_block_to_htmlnode(block))
        elif block_type_ordered_list == type_result:
            all_nodes.append(ol_block_to_htmlnode(block))
        else:
            all_nodes.append(paragraph_block_to_htmlnode(block))
    return ParentNode("div", all_nodes)


markdown = """# The Unparalleled Majesty of "The Lord of the Rings"

[Back Home](/)

![LOTR image artistmonkeys](/images/rivendell.png)

> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.
> I much prefer history, true or feigned, with its varied applicability to the thought and experience of readers.
> I think that many confuse 'applicability' with 'allegory'; but the one resides in the freedom of the reader, and the other in the purposed domination of the author."

In the annals of fantasy literature and the broader realm of creative world-building, few sagas can rival the intricate tapestry woven by J.R.R. Tolkien in *The Lord of the Rings*. You can find the [wiki here](https://lotr.fandom.com/wiki/Main_Page).

## Introduction

This series, a cornerstone of what I, in my many years as an **Archmage**, have come to recognize as the pinnacle of imaginative creation, stands unrivaled in its depth, complexity, and the sheer scope of its *legendarium*. As we embark on this exploration, let us delve into the reasons why this monumental work is celebrated as the finest in the world.

## A Rich Tapestry of Lore

One cannot simply discuss *The Lord of the Rings* without acknowledging the bedrock upon which it stands: **The Silmarillion**. This compendium of mythopoeic tales sets the stage for Middle-earth's history, from the creation myth of Eä to the epic sagas of the Elder Days. It is a testament to Tolkien's unparalleled skill as a linguist and myth-maker, crafting:

1. An elaborate pantheon of deities (the `Valar` and `Maiar`)
2. The tragic saga of the Noldor Elves
3. The rise and fall of great kingdoms such as Gondolin and Númenor

```
print("Lord")
print("of")
print("the")
print("Rings")
```

## The Art of **World-Building**

### Crafting Middle-earth
Tolkien's Middle-earth is a realm of breathtaking diversity and realism, brought to life by his meticulous attention to detail. This world is characterized by:

- **Diverse Cultures and Languages**: Each race, from the noble Elves to the sturdy Dwarves, is endowed with its own rich history, customs, and language. Tolkien, leveraging his expertise in philology, constructed languages such as Quenya and Sindarin, each with its own grammar and lexicon.
- **Geographical Realism**: The landscape of Middle-earth, from the Shire's pastoral hills to the shadowy depths of Mordor, is depicted with such vividness that it feels as tangible as our own world.
- **Historical Depth**: The legendarium is imbued with a sense of history, with ruins, artifacts, and lore that hint at bygone eras, giving the world a lived-in, authentic feel.

## Themes of *Timeless* Relevance

### The *Struggle* of Good vs. Evil

At its heart, *The Lord of the Rings* is a timeless narrative of the perennial struggle between light and darkness, a theme that resonates deeply with the human experience. The saga explores:

- The resilience of the human (and hobbit) spirit in the face of overwhelming odds
- The corrupting influence of power, epitomized by the One Ring
- The importance of friendship, loyalty, and sacrifice

These universal themes lend the series a profound philosophical depth, making it a beacon of wisdom and insight for generations of readers.

## A Legacy **Unmatched**

### The Influence on Modern Fantasy

The shadow that *The Lord of the Rings* casts over the fantasy genre is both vast and deep, having inspired countless authors, artists, and filmmakers. Its legacy is evident in:

- The archetypal "hero's journey" that has become a staple of fantasy narratives
- The trope of the "fellowship," a diverse group banding together to face a common foe
- The concept of a richly detailed fantasy world, which has become a benchmark for the genre

## Conclusion

As we stand at the threshold of this mystical realm, it is clear that *The Lord of the Rings* is not merely a series but a gateway to a world that continues to enchant and inspire. It is a beacon of imagination, a wellspring of wisdom, and a testament to the power of myth. In the grand tapestry of fantasy literature, Tolkien's masterpiece is the gleaming jewel in the crown, unmatched in its majesty and enduring in its legacy. As an Archmage who has traversed the myriad realms of magic and lore, I declare with utmost conviction: *The Lord of the Rings* reigns supreme as the greatest legendarium our world has ever known.

Splendid! Then we have an accord: in the realm of fantasy and beyond, Tolkien's creation is unparalleled, a treasure trove of wisdom, wonder, and the indomitable spirit of adventure that dwells within us all.
"""
test_node = markdown_to_htmlnode(markdown)
# html_result = test_node.to_html()
print(test_node)