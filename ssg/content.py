import re
from yaml import load
from yaml import FullLoader
from _collections_abc import Mapping

class Content(Mapping):
    __delimited = '"^(?:-|\+){3}\s*$"'
    __regex = re.compile(__delimited, re.MULTILINE)


    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data = {"content": content}

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if self.data.keys() is type else None

    @type.setter
    def type(self, value):
        self.type = self.data["type"]

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.__iter__()

    def __len__(self):
        return self.data.__len__()

    def __repr__(self):
        data = {}
        return str(data)
        for every in self.data.items():
            if key is not "content":
                value = data[key]


