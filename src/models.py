from dataclasses import dataclass

@dataclass
class Note:
    id: int
    title: str
    content: str