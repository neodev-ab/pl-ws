# Typescript testing

Please start by inspecting the `lexer.ts` and `lexer.test.ts` files in the current directory.

A `lexer.ts` has been prepared for you. Please complete the `tokenize(code: string) -> Token[]` function.

## Tests
In order to run the tests, just run `yarn test`.

If you wish to have the överkurs tests here are the options:
- string
- unary
- float
- identifier

These options are added as an environment variable. Like so:
```bash
TESTS=string,unary yarn test
```
