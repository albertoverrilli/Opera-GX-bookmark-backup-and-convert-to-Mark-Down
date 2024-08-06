import json

def convert_json_to_markdown(json_file, md_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print("JSON file read successfully")
        
        with open(md_file, 'w', encoding='utf-8') as file:
            process_bookmarks(data['roots']['bookmark_bar']['children'], file, 0)
        print(f"Markdown file created successfully at {md_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_bookmarks(bookmarks, file, level):
    indent = '  ' * level
    for bookmark in bookmarks:
        if bookmark['type'] == 'folder':
            folder_name = bookmark['name']
            print(f"Folder found: {folder_name}")
            file.write(f"{indent}- **{folder_name}**\n")
            process_bookmarks(bookmark['children'], file, level + 1)
        elif bookmark['type'] == 'url':
            title = bookmark['name']
            url = bookmark['url']
            print(f"Bookmark found: {title} - {url}")
            file.write(f"{indent}- [{title}]({url})\n")

# Define the paths for the JSON input file and the Markdown output file
json_bookmarks = r'C:\Users\alber\Documents\My Notebook\The AlgorIthm\Knowledge\Personal\Bookmarks\Bookmarks_Backup.html'
markdown_bookmarks = r'C:\Users\alber\Documents\My Notebook\The AlgorIthm\Knowledge\Personal\Bookmarks\Bookmarks.md'

convert_json_to_markdown(json_bookmarks, markdown_bookmarks)
