from typing import Tuple
from json import JSONEncoder, JSONDecoder

class Diary:
    def __init__(self):
        self._entries:list[Tuple[str,str]]|None = None
        self.entries = []

    @property
    def entries(self) -> list[Tuple[str,str]]:
        return self._entries

    @entries.setter
    def entries(self, val) -> None:
        self._entries = val

    def add(self, date, body) -> None:
        self.entries.append((date,body))

    def save(self, path) -> None:
        enc = JSONEncoder()
        json:str = enc.encode(self)
        fptr = open(path)
        fptr.write(json)
        fptr.close()

    def load(self, path):
        fptr = open(path)
        json:str = fptr.read()
        fptr.close()
        dec = JSONDecoder()
        return dec.decode(json)

