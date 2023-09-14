from typing import Tuple

class Diary:
    def __intit__(self):
        self.entries: Tuple[str,str] = []

    @property
    def entries(self) -> Tuple[str,str]:
        return self.entries

    def add(self, date, body) -> None:
        self.entries.append(Tuple(date,body))

