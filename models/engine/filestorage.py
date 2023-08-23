import os

class FileStorage:
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def save_file(self, filename, content):
        filepath = os.path.join(self.storage_path, filename)
        with open(filepath, "w") as file:
            file.write(content)

    def get_file(self, filename):
        filepath = os.path.join(self.storage_path, filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                return file.read()
        return None
