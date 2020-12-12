import os
class FileSystem:

    def ReadFile(self, file_path:str) -> str:
        if file_path is not None:
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf8') as reader:
                    return reader.read()
