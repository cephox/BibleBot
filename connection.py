import requests
import json


def get_bible_verse(book, chapter, verse, version=None):
    url = "https://getbible.net/json?passage=" + book + chapter + ":" + verse
    if version:
        url += "&v=" + version.lower()
    r = requests.get(url)
    data = r.text.replace("(", "", 1)[::-1].replace(")", "", 1).replace(";", "", 1)[::-1]
    return json.loads(data)


class BibleRequest:
    def __init__(self, book, chapter, verses, version=None):
        self.json = get_bible_verse(book, chapter, verses, version)
        self.books = self.json["book"]
        self.verses = dict()
        for i in self.books:
            chapter_data = i["chapter"]
            verse_indexes = [i for i in chapter_data]
            for j in verse_indexes:
                self.verses[j] = chapter_data[str(j)]["verse"].replace("\r\n", "")
