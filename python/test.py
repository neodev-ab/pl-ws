import unittest
from lexer import Token, TokenType, tokenize
import os

if "TESTS" in os.environ:
    over_course_string = "string" in os.environ["TESTS"]
    over_course_unary = "unary" in os.environ["TESTS"]
    over_course_float = "floats" in os.environ["TESTS"]
    over_course_identifier = "identifier" in os.environ["TESTS"]
else:
    over_course_string = False
    over_course_unary = False
    over_course_float = False
    over_course_identifier = False


# Unit tests
class TestTokenize(unittest.TestCase):

    def test_empty_string(self):
        code = ""
        expected_tokens = []
        self.assertEqual(tokenize(code), expected_tokens)

    def test_integer(self):
        code = "123"
        expected_tokens = [Token(TokenType.INTEGER, '123')]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_plus(self):
        code = "+"
        expected_tokens = [Token(TokenType.PLUS)]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_minus(self):
        code = "-"
        expected_tokens = [Token(TokenType.MINUS)]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_mul(self):
        code = "*"
        expected_tokens = [Token(TokenType.MUL)]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_div(self):
        code = "/"
        expected_tokens = [Token(TokenType.DIV)]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_addition_expression(self):
        code = "1 + 2"
        expected_tokens = [
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.PLUS),
            Token(TokenType.INTEGER, '2')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_multiple_expression(self):
        code = "1 + 2 * 3"
        expected_tokens = [
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.PLUS),
            Token(TokenType.INTEGER, '2'),
            Token(TokenType.MUL),
            Token(TokenType.INTEGER, '3')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_no_space_expression(self):
        code = "1+2*3"
        expected_tokens = [
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.PLUS),
            Token(TokenType.INTEGER, '2'),
            Token(TokenType.MUL),
            Token(TokenType.INTEGER, '3')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    @unittest.skipIf(not over_course_identifier, "Test skipped because it's an överkurs exercise")
    def test_identifier(self):
        code = "hello"
        expected_tokens = [Token(TokenType.IDENTIFIER, 'hello')]
        self.assertEqual(tokenize(code), expected_tokens)

    @unittest.skipIf(not over_course_float, "Test skipped because it's an överkurs exercise")
    def test_float(self):
        code = "123.456"
        expected_tokens = [Token(TokenType.FLOAT, '123.456')]
        self.assertEqual(tokenize(code), expected_tokens)

    @unittest.skipIf(not over_course_float, "Test skipped because it's an överkurs exercise")
    def test_float_addition(self):
        code = "123.456 + 789.123"
        expected_tokens = [
            Token(TokenType.FLOAT, '123.456'),
            Token(TokenType.PLUS),
            Token(TokenType.FLOAT, '789.123')
        ]
        self.assertEqual(tokenize(code), expected_tokens)


    @unittest.skipIf(not over_course_string, "Test skipped because it's an överkurs exercise")
    def test_string(self):
        code = "hello"
        expected_tokens = [Token(TokenType.STRING, 'hello')]
        self.assertEqual(tokenize(code), expected_tokens)

    @unittest.skipIf(not over_course_string, "Test skipped because it's an överkurs exercise")
    def test_string_addition(self):
        code = "hello + world"
        expected_tokens = [
            Token(TokenType.STRING, 'hello'),
            Token(TokenType.PLUS),
            Token(TokenType.STRING, 'world')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    @unittest.skipIf(not over_course_unary, "Test skipped because it's an överkurs exercise")
    def test_increment(self):
        code = "++"
        expected_tokens = [Token(TokenType.INCREMENT)]
        self.assertEqual(tokenize(code), expected_tokens)

    @unittest.skipIf(not over_course_unary, "Test skipped because it's an överkurs exercise")
    def test_increment_expression(self):
        code = "1++"
        expected_tokens = [
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.INCREMENT)
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    @unittest.skipIf(not over_course_unary, "Test skipped because it's an överkurs exercise")
    def test_increment_expression_with_space(self):
        code = "1 ++ + 2"
        expected_tokens = [
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.INCREMENT),
            Token(TokenType.PLUS)
        ]
        self.assertEqual(tokenize(code), expected_tokens)



if __name__ == "__main__":
    unittest.main()
