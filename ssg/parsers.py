from typing import List
from pathlib import Path
import shutil


class Parser:
    extensions = List[str]  # type List[str]

    def valid_extension(self, extension):
        self.extension = extension
        isinstance(self.extension, extensions)

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file

    def write(self, path, dest, content, ext=".html"):
        self.path = path
        self.dest = dest
        self.content = content
        full_path = self.dest / with_suffix.self.path(ext)
        with open(full_path) as file:
            file = self.content

    def copy(self, path, source, dest):
        self.path = path
        self.source = source
        self.dest = dest
        shutil.copy2(self.path, self.dest / self.source)


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        super().copy(path, source, dest)

