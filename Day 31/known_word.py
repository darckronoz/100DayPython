from typing import NamedTuple

class KnownWord(NamedTuple):
    score: int
    last_studied: str
    rank: int #index unique identifier
