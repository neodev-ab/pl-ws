type TokenType =
  | "INTEGER"
  | "FLOAT"
  | "PLUS"
  | "MINUS"
  | "MUL"
  | "DIV"
  | "STRING"
  | "IDENTIFIER"
  | "INCREMENT";

type Token = {
  type: TokenType;
  value?: string;
};

export function tokenize(code: string): Token[] {
  return [];
}
