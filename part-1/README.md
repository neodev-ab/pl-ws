# Let's implement a lexer!
A lexer (short for lexical analyzer) is a fundamental component in compiler construction and text processing. Its primary function is to break down a sequence of characters (usually source code or textual data) into a series of tokens, which are meaningful units such as keywords, identifiers, operators, and punctuation.

## How a Lexer Works:

Input: Receives a stream of characters as input.

Tokenization: Processes the input by recognizing and categorizing sequences of characters into tokens based on predefined rules (patterns or regular expressions).

Token Output: Outputs these tokens along with their respective types for further processing by a parser or another component in the compiler or text processing pipeline.

## Tokenization Example
Given the expression:

```python
10 + 3.5 - y * 2.7
```
**Tokenization Output:**
- `Token(INTEGER, "10")`: Represents the integer literal 10.
- `Token(PLUS)`: Represents the addition operator +.
- `Token(FLOAT, "3.5")`: Represents the floating-point literal 3.5.
- `Token(MINUS)`: Represents the subtraction operator -.
- `Token(IDENTIFIER, "y")`: Represents the identifier y.
- `Token(MUL)`: Represents the multiplication operator *.
- `Token(FLOAT, "2.7")`: Represents the floating-point literal 2.7.
