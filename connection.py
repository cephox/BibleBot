import requests
import json


def get_bible_verse(book, chapter, verse):
    url = "https://getbible.net/json?passage=" + book + chapter + ":" + verse
    r = requests.get(url)
    data = r.text.replace("(", "", 1)[::-1].replace(")", "", 1).replace(";", "", 1)[::-1]
    return json.loads(data)


class BibleRequest:
    def __init__(self, book, chapter, verses):
        self.json = get_bible_verse(book, chapter, verses)
        self.books = self.json["book"]
        self.verses = dict()
        for i in self.books:
            chapter_data = i["chapter"]
            verse_indexes = [i for i in chapter_data]
            for j in verse_indexes:
                self.verses[j] = chapter_data[str(j)]["verse"].replace("\r\n", "")
