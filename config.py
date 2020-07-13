import json


class Config:
    def __init__(self, filename):
        self.filename = filename
        self._data = json.load(open(filename))

    def save(self, key, value):
        self._data = json.load(open(self.filename))
        self._data[key] = value
        json.dump(self._data, open(self.filename, "w"), indent=4)

    def __getattr__(self, item: str):
        if item.startswith("f_"):
            return self._data[item[2:]].format
        return self._data[item]
