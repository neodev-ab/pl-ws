import unittest
from parser import *
from lexer import *

class TestParser(unittest.TestCase):
    """
    `ts` stands for token stream.
    """
    def test_empty_ts(self):
        ts = []
        try:
            parse(ts)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_integer(self):
        ts = [Token(TokenType.INTEGER, '123')]
        self.assertEqual(parse(ts), Primary(TokenType.INTEGER, '123'))

    def test_only_operator(self):
        try:
            parse([Token(TokenType.PLUS)])
            self.assertTrue(False)
        except:
            self.assertTrue(True)

        try:
            parse([Token(TokenType.MINUS)])
            self.assertTrue(False)
        except:
            self.assertTrue(True)

        try:
            parse([Token(TokenType.MUL)])
            self.assertTrue(False)
        except:
            self.assertTrue(True)

        try:
            parse([Token(TokenType.DIV)])
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_addition_expression(self):
        ts = [
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.PLUS),
            Token(TokenType.INTEGER, '2')
        ]
        self.assertEqual(parse(ts),
                        BinaryOperation(TokenType.PLUS,
                            Primary(TokenType.INTEGER, '1'),
                            Primary(TokenType.INTEGER, '2')))

    def test_multiple_additions_expression(self):
        ts = [
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.PLUS),
            Token(TokenType.INTEGER, '2'),
            Token(TokenType.PLUS),
            Token(TokenType.INTEGER, '3')
        ]
        self.assertEqual(parse(ts),
                         BinaryOperation(TokenType.PLUS,
                            BinaryOperation(TokenType.PLUS,
                                Primary(TokenType.INTEGER, '1'),
                                Primary(TokenType.INTEGER, '2')),
                            Primary(TokenType.INTEGER, '3')))

    def test_operator_precedence(self):
        ts = [
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.PLUS),
            Token(TokenType.INTEGER, '2'),
            Token(TokenType.MUL),
            Token(TokenType.INTEGER, '3')
        ]
        self.assertEqual(parse(ts),
                         BinaryOperation(TokenType.PLUS,
                            Primary(TokenType.INTEGER, '1'),
                            BinaryOperation(TokenType.MUL,
                                Primary(TokenType.INTEGER, '2'),
                                Primary(TokenType.INTEGER, '3'))))

    def test_unary_operator(self):
        ts = [
            Token(TokenType.INCREMENT),
            Token(TokenType.INTEGER, '1')
        ]
        self.assertEqual(parse(ts),
                            UnaryOperation(TokenType.INCREMENT,
                                Primary(TokenType.INTEGER, '1')))

    def test_unary_operator_precedence(self):
        ts = [
            Token(TokenType.INCREMENT),
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.PLUS),
            Token(TokenType.INTEGER, '2')
        ]
        self.assertEqual(parse(ts),
                            BinaryOperation(TokenType.PLUS,
                                UnaryOperation(TokenType.INCREMENT, Primary(TokenType.INTEGER, '1')),
                                Primary(TokenType.INTEGER, '2')))
