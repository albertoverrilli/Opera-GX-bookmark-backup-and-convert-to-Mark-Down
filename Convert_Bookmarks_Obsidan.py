import json
import os

def convert_json_to_structure_and_markdown(json_file, base_dir, md_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print("JSON file read successfully")
        
        # Process bookmarks to create folder structure and save individual files
        process_bookmarks(data['roots']['bookmark_bar']['children'], base_dir, None)
        
        # Process bookmarks to create a single Markdown file
        with open(md_file, 'w', encoding='utf-8') as file:
            process_bookmarks_for_md(data['roots']['bookmark_bar']['children'], file, 0)
            file.write("\n***\n[[Bookmarks]]")
        print(f"Markdown file created successfully at {md_file}")
        print(f"Bookmarks successfully saved in directories at {base_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_bookmarks(bookmarks, current_dir, parent_folder):
    if not os.path.exists(current_dir):
        os.makedirs(current_dir)
    
    for bookmark in bookmarks:
        if bookmark['type'] == 'folder':
            folder_name = sanitize_filename(bookmark['name'])
            folder_path = os.path.join(current_dir, folder_name)
            print(f"Creating folder: {folder_path}")
            process_bookmarks(bookmark['children'], folder_path, folder_name)
            save_folder_markdown(folder_path, folder_name, parent_folder)
        elif bookmark['type'] == 'url':
            title = sanitize_filename(bookmark['name'])
            url = bookmark['url']
            print(f"Saving bookmark: {title} - {url}")
            save_bookmark(current_dir, title, url, parent_folder)

def process_bookmarks_for_md(bookmarks, file, level):
    indent = '  ' * level
    for bookmark in bookmarks:
        if bookmark['type'] == 'folder':
            folder_name = bookmark['name']
            print(f"Folder found: {folder_name}")
            file.write(f"{indent}- **{folder_name}**\n")
            process_bookmarks_for_md(bookmark['children'], file, level + 1)
        elif bookmark['type'] == 'url':
            title = bookmark['name']
            url = bookmark['url']
            print(f"Bookmark found: {title} - {url}")
            file.write(f"{indent}- [{title}]({url})\n")

def save_folder_markdown(directory, folder_name, parent_folder):
    file_path = os.path.join(directory, f"{folder_name}.md")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"[[{parent_folder}]]\n")
        file.write(f"\n***\n[[Personal]]")

def save_bookmark(directory, title, url, parent_folder):
    file_path = os.path.join(directory, f"{title}.md")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"[{title}]({url})\n")
        file.write(f"\n***\n[[{parent_folder}]]")

def sanitize_filename(name):
    # Sanitize filenames to avoid invalid characters
    return "".join(c for c in name if c.isalnum() or c in (' ', '-', '_')).rstrip()

# Define the paths for the JSON input file, base directory for output, and the single Markdown file
json_bookmarks = r'C:\Users\alber\Documents\My Notebook\The AlgorIthm\Knowledge\Personal\Bookmarks\Bookmarks_Backup.html'
base_directory = r'C:\Users\alber\Documents\My Notebook\The AlgorIthm\Knowledge\Personal\Bookmarks\Bookmarks_Folders'
markdown_bookmarks = r'C:\Users\alber\Documents\My Notebook\The AlgorIthm\Knowledge\Personal\Bookmarks\Bookmarks.md'

convert_json_to_structure_and_markdown(json_bookmarks, base_directory, markdown_bookmarks)
