import os


class FileBrowser:
    def __init__(self):
        os.chdir("\\")
        print(os.getcwd())

    @property
    def cwd(self) -> str:
        return os.getcwd()


    def show_directory(self, absolute_path:str = None) -> str:
        print(os.getcwd())
        absolute_path = os.getcwd() if absolute_path is None else absolute_path
        dir_items = os.listdir(absolute_path)
        return f"Directory: {absolute_path} contains: {len(dir_items)}: items\n {dir_items}"


    def open_directory(self, chosen_file: str) -> str:
        absolute_path = os.path.join(self.cwd, chosen_file)
        items_in_dir = os.listdir(self.cwd)
        if chosen_file not in items_in_dir:
            raise FileNotFoundError(f"the chosen item {chosen_file} is not found")
        elif chosen_file in items_in_dir and os.path.isfile(absolute_path):
            raise NotADirectoryError(f"the chosen item {chosen_file} is a file")
        os.chdir(absolute_path)



    def get_file_path(self, chosen_file: str) -> str:
        absolute_path = os.path.join(self.cwd, chosen_file)
        if chosen_file in os.listdir() and os.path.isfile(absolute_path):
            return absolute_path
        raise FileNotFoundError(f"the chosen item {chosen_file} is not file")





