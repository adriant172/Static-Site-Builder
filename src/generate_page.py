from block_markdown import markdown_to_htmlnode
import os


def extract_title(markdown):
    """This extracts the H1 header line from a markdown file"""
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("#") and line[1] != "#":
            return line
    raise ValueError("No title exists.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path, 'r', encoding="utf-8")
    markdown = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path, 'r', encoding='utf-8')
    template = template_file.read()
    template_file.close()
    html_content = markdown_to_htmlnode(markdown)
    html_content = html_content.to_html()
    page_title = extract_title(markdown)
    new_page = template.replace("{{ Title }}", page_title).replace("{{ Content }}", html_content)
    if os.path.exists(os.path.dirname(dest_path)) is False:
        os.makedirs(os.path.dirname(dest_path))
    destination_file = open(dest_path, 'w', encoding='utf-8')
    destination_file.write(new_page)
    destination_file.close()
    print(new_page)


    
