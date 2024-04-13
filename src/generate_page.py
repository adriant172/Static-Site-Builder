from block_markdown import markdown_to_htmlnode
from pathlib import Path
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
    """Generates a single html page from a markdown file"""
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

def generates_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """Generates multiple html pages from multiple markdown files nested within
      all sub-directories of the targeted directory"""
    dir_path_object = Path(dir_path_content)
    if dir_path_object.is_dir() and dir_path_object.exists():
        dir_contents = os.listdir(dir_path_content)
        for item in dir_contents:
            source_path = os.path.join(dir_path_content, item)
            if os.path.isfile(source_path) and item.endswith(".md"):
                file = item[:-2]
                file += "html"
                destination_path =os.path.join(dest_dir_path, file)
                generate_page(source_path,template_path, destination_path)
            else:
                destination_path =os.path.join(dest_dir_path, item)
                os.mkdir(destination_path)
                generates_pages_recursive(source_path, template_path, destination_path)
