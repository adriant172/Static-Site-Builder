import re 

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    if len(matches) == 0:
        raise Exception("No markdown images found.")
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    if len(matches) == 0:
        raise Exception("No markdown images found.")
    return matches




# extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)")
# print("---------------------------------------------")
# extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)")