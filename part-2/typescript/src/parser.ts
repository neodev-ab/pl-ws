import { Token } from "./lexer";

type TPrimary = "INTEGER" | "FLOAT" | "STRING" | "IDENTIFIER";
type TBinaryOperator = "PLUS" | "MINUS" | "MUL" | "DIV";
type TUnaryOperator = "INCREMENT";

type Primary = {
  type: "Primary";
  dataType: TPrimary;
  value: string
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
  return {} as Expression;
}
