from typing import List
from pathlib import Path
import shutil


class Parser:
    #extensions = List[str]  # type List[str]
    extensions: List[str] = []

    def valid_extension(self, extension):
       # self.extension = extension
       # isinstance(self.extension, extensions)
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return file

    def write(self, path, dest, content, ext=".html"):
        self.path = path
        self.dest = dest
        self.content = content
        full_path = self.dest / self.path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(self.content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / source)


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        super().copy(path, source, dest)

