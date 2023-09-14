from typing import Tuple
from json import JSONEncoder, JSONDecoder

class Diary:
    def __intit__(self):
        self.entries: Tuple[str,str] = []

    @property
    def entries(self) -> Tuple[str,str]:
        return self.entries

    def add(self, date, body) -> None:
        self.entries.append(Tuple(date,body))

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

