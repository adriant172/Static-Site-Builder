from generate_page import generate_page
from copy_static import copy_dir, clear_dir

static_path = "./static"
public_path = "./public"

def main():
    clear_dir(public_path)
    copy_dir(static_path, public_path)
    generate_page("./content/index.md", "./template.html", "./public/index.html")

main()