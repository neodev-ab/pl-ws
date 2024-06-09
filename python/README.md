# Python testing

Please start by inspecting the `lexer.py` and `test.py` files in the current directory.

A `lexer.py` has been prepared for you. Please complete the `tokenize(code: str) -> list[Token]` function.

## Tests
In order to run the tests, just run `python test.py`.

If you wish to have the överkurs tests here are the options:
- string
- unary
- float
- identifier

These options are added as an environment variable. Like so:
```bash
TESTS=string,unary python test.py
```
