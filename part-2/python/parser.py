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

def parse(tokens: List[Token]) -> Expression:
    index = 0

    def peek() -> Optional[Token]:
        if index >= len(tokens):
            return None
        return tokens[index]

    def consume() -> Optional[Token]:
        nonlocal index
        if index >= len(tokens):
            return None
        token = tokens[index]
        index += 1
        return token

    def parse_primary() -> Primary:
        token = consume()
        if not token:
            raise Exception("Unexpected end of tokens")
        if token.type in (TokenType.INTEGER, TokenType.FLOAT, TokenType.STRING, TokenType.IDENTIFIER) and token.value:
            return Primary(token.type, token.value)
        raise Exception(f"Unexpected token {token}")

    def parse_unary() -> Expression:
        peeked = peek()
        if peeked and peeked.type == TokenType.INCREMENT:
            consume()
            return UnaryOperation(peeked.type, parse_primary())
    
        expression = parse_primary()
        while True:
            operator = peek()
            if operator and operator.type == TokenType.INCREMENT:
                consume()
                expression = UnaryOperation(operator.type, expression)
            else:
                break

        return expression

    def parse_factor() -> Expression:
        expression = parse_unary()

        while True:
            operator = peek()
            if operator and operator.type in (TokenType.MUL, TokenType.DIV):
                consume()
                right = parse_unary()
                expression = BinaryOperation(operator.type, expression, right)
            else:
                break

        return expression

    def parse_term() -> Expression:
        expression = parse_factor()

        while True:
            operator = peek()
            if operator and operator.type in (TokenType.PLUS, TokenType.MINUS):
                consume()
                right = parse_factor()
                expression = BinaryOperation(operator.type, expression, right)
            else:
                break

        return expression

    def parse_expression() -> Expression:
        return parse_term()

    return parse_expression()

if __name__ == '__main__':
    tokens = [
        Token(TokenType.INTEGER, '1'),
        Token(TokenType.PLUS),
        Token(TokenType.INTEGER, '2'),
        Token(TokenType.MUL),
        Token(TokenType.INTEGER, '3')
    ]
    print(parse(tokens))
