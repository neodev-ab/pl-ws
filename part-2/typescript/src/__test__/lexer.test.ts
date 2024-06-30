import { expect, describe, it } from "@jest/globals";
import { tokenize } from "../lexer";

describe("tokenizer", () => {
  it("empty string", () => {
    expect(tokenize("")).toEqual([]);
  });

  it("integer", () => {
    expect(tokenize("123")).toEqual([{ type: "INTEGER", value: "123" }]);
  });

  it("plus", () => {
    expect(tokenize("+")).toEqual([{ type: "PLUS" }]);
  });

  it("minus", () => {
    expect(tokenize("-")).toEqual([{ type: "MINUS" }]);
  });

  it("mul", () => {
    expect(tokenize("*")).toEqual([{ type: "MUL" }]);
  });

  it("div", () => {
    expect(tokenize("/")).toEqual([{ type: "DIV" }]);
  });

  it("addition expression", () => {
    expect(tokenize("1 + 2")).toEqual([
      { type: "INTEGER", value: "1" },
      { type: "PLUS" },
      { type: "INTEGER", value: "2" },
    ]);
  });

  it("multiple expression", () => {
    expect(tokenize("1 + 2 * 3")).toEqual([
      { type: "INTEGER", value: "1" },
      { type: "PLUS" },
      { type: "INTEGER", value: "2" },
      { type: "MUL" },
      { type: "INTEGER", value: "3" },
    ]);
  });

  it("no space expression", () => {
    expect(tokenize("1+2*3")).toEqual([
      { type: "INTEGER", value: "1" },
      { type: "PLUS" },
      { type: "INTEGER", value: "2" },
      { type: "MUL" },
      { type: "INTEGER", value: "3" },
    ]);
  });

  it("identifier", () => {
    expect(tokenize("x")).toEqual([{ type: "IDENTIFIER", value: "x" }]);
  });

  it("float", () => {
    expect(tokenize("123.456")).toEqual([{ type: "FLOAT", value: "123.456" }]);
  });

  it("float addition", () => {
    expect(tokenize("123.456 + 789.123")).toEqual([
      { type: "FLOAT", value: "123.456" },
      { type: "PLUS" },
      { type: "FLOAT", value: "789.123" },
    ]);
  });

  it("string", () => {
    expect(tokenize('"Hello world!"')).toEqual([
      { type: "STRING", value: "Hello world!" },
    ]);
  });

  it("string addition", () => {
    expect(tokenize('"hello" + "world"')).toEqual([
      { type: "STRING", value: "hello" },
      { type: "PLUS" },
      { type: "STRING", value: "world" },
    ]);
  });

  it("increment", () => {
    expect(tokenize("++")).toEqual([{ type: "INCREMENT" }]);
  });

  it("increment expression", () => {
    expect(tokenize("1++")).toEqual([
      { type: "INTEGER", value: "1" },
      { type: "INCREMENT" },
    ]);
  });

  it("increment expression with space", () => {
    expect(tokenize("1 ++ + 2")).toEqual([
      { type: "INTEGER", value: "1" },
      { type: "INCREMENT" },
      { type: "PLUS" },
      { type: "INTEGER", value: "2" },
    ]);
  });
});
