# Define the source path for Opera GX bookmarks
$sourcePath = "C:\Users\alber\AppData\Roaming\Opera Software\Opera GX Stable\Bookmarks"

# Define the destination path for the backup
$destinationPath = "C:\Users\alber\Documents\My Notebook\The AlgorIthm\Knowledge\Personal\Bookmarks\Bookmarks_Backup.html"

# Copy the bookmarks file to the backup location
Copy-Item -Path $sourcePath -Destination $destinationPath -Force


# Run the Python script to convert the HTML bookmarks to Markdown
$pythonScriptPath = "C:\Users\alber\Documents\My Notebook\The AlgorIthm\Knowledge\Personal\Bookmarks\Convert_Bookmarks.py"
python $pythonScriptPath