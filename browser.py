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
        return f"Directory: {absolute_path} items of len {len(dir_items)}:\n {dir_items}"


    def open(self, chosen_file: str) -> str:
        absolute_path = os.path.join(self.cwd, chosen_file)
        if not os.path.isdir(absolute_path):
            return f"the chosen item {chosen_file} is not directory"
        if chosen_file not in os.listdir(self.cwd):
            return f"the chosen directory {chosen_file} not found"
        os.chdir(absolute_path)
        return self.show_directory(absolute_path)

    def get_file_path(self, chosen_file: str) -> str:
        absolute_path = os.path.join(self.cwd, chosen_file)
        if chosen_file in os.listdir() and os.path.isfile(absolute_path):
            return absolute_path
        return f"the chosen item {chosen_file} is not file"




