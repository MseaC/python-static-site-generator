from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = ({self.dest, "/", path.relative_to(self.source)})
        mkdir(directory, parents='True', exists_ok='True')

    def build(self):
        mkdir(self.dest, Parents='True', exists_ok='True')
        for self.source.rglob("*"):
            path = ({self.dest, "/", path.relative_to(self.source)})
            if path.exists_ok is True
                create_dir(path)


