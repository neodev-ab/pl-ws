from typing import Union, Literal, List
from lexer import *

# Types
TBinaryOperator = Union[
    Literal[TokenType.PLUS],
    Literal[TokenType.MINUS],
    Literal[TokenType.MUL],
    Literal[TokenType.DIV]]

TUnaryOperator = Literal[TokenType.INCREMENT]

TPrimary = Union[
    Literal[TokenType.INTEGER],
    Literal[TokenType.FLOAT],
    Literal[TokenType.STRING],
    Literal[TokenType.IDENTIFIER]]

Expression = Union['Primary', 'BinaryOperation', 'UnaryOperation']

# Nodes
class Primary:

    def __init__(self, type: TPrimary, value: str):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"Primary({self.value})"

    def __eq__(self, other):
        if not isinstance(other, Primary):
            return False
        return self.type == other.type and self.value == other.value

class BinaryOperation:
    
    def __init__(self,
                 operator: TBinaryOperator,
                 left: Expression,
                 right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f'({self.left} {self.operator} {self.right})'
    
    def __repr__(self) -> str:
        return f"BinaryOperation({self.left}, {self.operator}, {self.right})"

    def __eq__(self, other):
        if not isinstance(other, BinaryOperation):
            return False
        return self.left == other.left and self.operator == other.operator and self.right == other.right

class UnaryOperation:
    
    def __init__(self,
                 operator: TUnaryOperator,
                 operand: Expression):
        self.operator = operator
        self.operand = operand

    def __str__(self):
        return f'{self.operator}{self.operand}'
    
    def __repr__(self) -> str:
        return f"UnaryOperation({self.operator}, {self.operand})"

    def __eq__(self, other):
        if not isinstance(other, UnaryOperation):
            return False
        return self.operator == other.operator and self.operand == other.operand

def parse(tokens: List[Token]) -> Expression: # type: ignore
    _ = tokens
