from typing import Optional
from enum import Enum, auto

class TokenType(Enum):
    INTEGER = auto()
    FLOAT = auto()
    PLUS = auto()
    MINUS = auto()
    MUL = auto()
    DIV = auto()
    STRING = auto() 
    IDENTIFIER = auto()
    INCREMENT = auto()

    def __str__(self):
        return self.name

class Token:
    def __init__(self, type: TokenType, value: Optional[str] = None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value is None:
            return f"Token({self.type})"
        return f"Token({self.type}, {self.value})"

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value


def tokenize(code: str) -> list[Token]:
    # Your code goes here
    return []
