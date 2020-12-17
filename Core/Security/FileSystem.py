import os


class FileSystem:

    def readfile(self, file_path: str) -> str:
        if file_path is not None:
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf8') as reader:
                    return reader.read()

    def append(self, file_path: str, content: str) -> bool:
        if file_path is not None and content is not None:
            with open(file_path, 'a', encoding='utf8') as appender:
                appender.write(content+'\n')
                return True
        return False

    def appendToFile(self, file_path: str, content: str, duplicate=True) -> bool:
        if duplicate:
            return self.append(file_path, content)
        else:
            file_content = self.readfile(file_path)
            if content not in file_content:
                return self.append(file_path, content)
        return False

    def writeToFile(self, file_path: str, content: str) -> bool:
        if file_path is not None and content is not None:
            with open(file_path, 'w', encoding='utf8') as writer:
                writer.write(content)
                return True
        return False
