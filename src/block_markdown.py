
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

markdown_file = """This is **bolded** paragraph
        



                        This is another paragraph with *italic* text and `code` here
                        This is the same paragraph on a new line

                        






                        * This is a list
                        * with items
                        """

blocks = markdown_to_blocks(markdown_file)
print(blocks)