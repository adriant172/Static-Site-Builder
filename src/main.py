from generate_page import generates_pages_recursive
from copy_static import copy_dir, clear_dir

static_path = "./static"
public_path = "./public"
content_path = "./content"
template_file_path = "./template.html"

def main():
    clear_dir(public_path)
    copy_dir(static_path, public_path)
    generates_pages_recursive(content_path, template_file_path , public_path)

main()