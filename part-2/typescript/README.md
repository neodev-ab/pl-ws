# Typescript!

## Step 1
A lexer has been implemented for you and resides in `src/lexer.ts`.
**Start by understanding how it works.**

## Step 2
During this session, we'll implement a parser! That is, a function that takes a stream of tokens and returns an abstract syntax tree (AST).

**Please start by inspecting the `src/parser.ts` and `src/__test__/parser.test.ts` files in the current directory.**

## Step 3
Let's start with a sanity check! Before you start implementing anything run the lexer-tests, 
**Run the lexer tests using:**
```bash
yarn jest -- src/__test__/lexer.test.ts
```

## Step 4:
Your task is be to implement the body of `parse(tokens: Token[]): Expression` function. 
During the course of development, you are encouraged to run the tests to make sure that you are moving in the right direction!
```bash
yarn jest -- src/__test__/parser.test.ts
```
