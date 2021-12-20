from browser import FileBrowser
f = FileBrowser()
print(f.show_directory())
f.open_directory("Users")
print(f.show_directory())
f.open_directory("User")
print(f.show_directory())
f.open_directory("Downloads")
print(f.show_directory())
print(f.open_directory("(1) WhatsApp.html"))
print(f.get_file_path("(1) WhatsApp.html"))

