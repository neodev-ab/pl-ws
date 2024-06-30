export type TokenType =
  | "INTEGER"
  | "FLOAT"
  | "PLUS"
  | "MINUS"
  | "MUL"
  | "DIV"
  | "STRING"
  | "IDENTIFIER"
  | "INCREMENT";

export type Token = {
  type: TokenType;
  value?: string;
};

export function tokenize(code: string): Token[] {
  const tokens: Token[] = [];
  let i = 0;

  while (i < code.length) {
    if (/\s/.test(code[i])) {
      i++;
      continue;
    }

    if (/\d/.test(code[i])) {
      let start = i;
      while (i < code.length && (/\d/.test(code[i]) || code[i] === '.')) {
        i++;
      }
      const value = code.slice(start, i);
      tokens.push({type: value.includes('.') ? "FLOAT" : "INTEGER", value});
      continue;
    }

    if (/[a-zA-Z]/.test(code[i])) {
      let start = i;
      while (i < code.length && /[a-zA-Z0-9]/.test(code[i])) {
        i++;
      }
      const value = code.slice(start, i);
      tokens.push({type: "IDENTIFIER", value});
      continue;
    }

    switch (code[i]) {
      case '+':
        if (i + 1 < code.length && code[i + 1] === '+') {
          tokens.push({type: "INCREMENT"});
          i++;
        } else {
          tokens.push({type: "PLUS"});
        }
        break;
      case '-':
        tokens.push({type: "MINUS"});
        break;
      case '*':
        tokens.push({type: "MUL"});
        break;
      case '/':
        tokens.push({type: "DIV"});
        break;
      case '"':
        let start = i + 1;
        i++;
        while (i < code.length && code[i] !== '"') {
          i++;
        }
        const stringValue = code.slice(start, i);
        tokens.push({type: "STRING", value: stringValue});
        break;
      default:
        throw new Error(`Unexpected character: ${code[i]}`);
    }

    i++;
  }

  return tokens;
}
