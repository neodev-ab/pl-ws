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
    tokens = []
    i = 0
    while i < len(code):
        if code[i].isdigit():
            start = i
            while i < len(code) and (code[i].isdigit() or code[i] == '.'):
                i += 1
            tokens.append(Token(TokenType.FLOAT if '.' in code[start:i] else TokenType.INTEGER, code[start:i]))
            continue
        if code[i] == '+':
            if i+1 < len(code) and code[i+1] == '+':
                tokens.append(Token(TokenType.INCREMENT))
                i += 1
            else:
                tokens.append(Token(TokenType.PLUS))
        elif code[i] == '-':
            tokens.append(Token(TokenType.MINUS))
        elif code[i] == '*':
            tokens.append(Token(TokenType.MUL))
        elif code[i] == '/':
            tokens.append(Token(TokenType.DIV))
        elif code[i] == '"':
            start = i
            i += 1
            while i < len(code) and code[i] != '"':
                i += 1
            tokens.append(Token(TokenType.STRING, code[start+1:i]))
        elif code[i].isalpha():
            start = i
            while i < len(code) and code[i].isalnum():
                i += 1
            tokens.append(Token(TokenType.IDENTIFIER, code[start:i]))
            continue
        i += 1

    return tokens
