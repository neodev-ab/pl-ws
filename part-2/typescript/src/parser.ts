import { Token } from "./lexer";

type TPrimary = "INTEGER" | "FLOAT" | "STRING" | "IDENTIFIER";
type TBinaryOperator = "PLUS" | "MINUS" | "MUL" | "DIV";
type TUnaryOperator = "INCREMENT";

type Primary = {
  type: "Primary";
  dataType: TPrimary;
  value: string;
};

type BinaryOperation = {
  type: "BinaryOperation";
  left: Expression;
  operator: TBinaryOperator;
  right: Expression;
};

type UnaryOperation = {
  type: "UnaryOperation";
  operator: TUnaryOperator;
  operand: Expression;
};

type Expression = Primary | BinaryOperation | UnaryOperation;

export function parse(tokens: Token[]): Expression {
  let index = 0;

  function peek(): Token | undefined {
    return tokens[index];
  }

  function consume(): Token | undefined {
    const token = tokens[index];
    index += 1;
    return token;
  }

  function parsePrimary(): Primary {
    const token = consume();
    if (!token) {
      throw new Error("Unexpected end of tokens");
    }
    if (["INTEGER", "FLOAT", "STRING", "IDENTIFIER"].includes(token.type)) {
      return {
        type: "Primary",
        dataType: token.type as TPrimary,
        value: token.value
      };
    }
    throw new Error(`Unexpected token ${token.type}`);
  }

  function parseUnary(): Expression {
    const token = peek();
    if (token && token.type === "INCREMENT") {
      consume();
      return {
        type: "UnaryOperation",
        operator: "INCREMENT",
        operand: parsePrimary()
      };
    }
    return parsePrimary();
  }

  function parseFactor(): Expression {
    let expression = parseUnary();
    while (true) {
      const token = peek();
      if (token && (token.type === "MUL" || token.type === "DIV")) {
        consume();
        const right = parseUnary();
        expression = {
          type: "BinaryOperation",
          left: expression,
          operator: token.type as TBinaryOperator,
          right
        };
      } else {
        break;
      }
    }
    return expression;
  }

  function parseTerm(): Expression {
    let expression = parseFactor();
    while (true) {
      const token = peek();
      if (token && (token.type === "PLUS" || token.type === "MINUS")) {
        consume();
        const right = parseFactor();
        expression = {
          type: "BinaryOperation",
          left: expression,
          operator: token.type as TBinaryOperator,
          right
        };
      } else {
        break;
      }
    }
    return expression;
  }

  function parseExpression(): Expression {
    return parseTerm();
  }

  if (tokens.length === 0) {
    throw new Error("Empty token stream");
  }

  return parseExpression();
}
