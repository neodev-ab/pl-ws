import { expect, describe, it } from "@jest/globals";
import { parse } from "../parser";
import { Token } from "../lexer";
import { fail } from "assert";

describe("TestParser", () => {
  it("test_empty_ts", () => {
    const ts: Token[] = [];
    try {
      parse(ts);
      fail("Expected an error to be thrown");
    } catch (e) {}
  });

  it("test_integer", () => {
    const ts: Token[] = [{ type: "INTEGER", value: "123" }];
    const expected = {
      type: "Primary",
      dataType: "INTEGER",
      value: "123",
    };
    expect(parse(ts)).toEqual(expected);
  });

  it("test_only_operator", () => {
    try {
      parse([{ type: "PLUS" }]);
      fail("Expected an error to be thrown");
    } catch (e) {}

    try {
      parse([{ type: "MINUS" }]);
      fail("Expected an error to be thrown");
    } catch (e) {}

    try {
      parse([{ type: "MUL" }]);
      fail("Expected an error to be thrown");
    } catch (e) {}

    try {
      parse([{ type: "DIV" }]);
      fail("Expected an error to be thrown");
    } catch (e) {}
  });

  it("test_addition_expression", () => {
    const ts: Token[] = [
      { type: "INTEGER", value: "1" },
      { type: "PLUS" },
      { type: "INTEGER", value: "2" },
    ];
    const expected = {
      type: "BinaryOperation",
      left: {
        type: "Primary",
        dataType: "INTEGER",
        value: "1",
      },
      operator: "PLUS",
      right: {
        type: "Primary",
        dataType: "INTEGER",
        value: "2",
      },
    };
    expect(parse(ts)).toEqual(expected);
  });

  it("test_multiple_additions_expression", () => {
    const ts: Token[] = [
      { type: "INTEGER", value: "1" },
      { type: "PLUS" },
      { type: "INTEGER", value: "2" },
      { type: "PLUS" },
      { type: "INTEGER", value: "3" },
    ];
    const expected = {
      type: "BinaryOperation",
      left: {
        type: "BinaryOperation",
        left: {
          type: "Primary",
          dataType: "INTEGER",
          value: "1",
        },
        operator: "PLUS",
        right: {
          type: "Primary",
          dataType: "INTEGER",
          value: "2",
        },
      },
      operator: "PLUS",
      right: {
        type: "Primary",
        dataType: "INTEGER",
        value: "3",
      },
    };
    expect(parse(ts)).toEqual(expected);
  });

  it("test_operator_precedence", () => {
    const ts: Token[] = [
      { type: "INTEGER", value: "1" },
      { type: "PLUS" },
      { type: "INTEGER", value: "2" },
      { type: "MUL" },
      { type: "INTEGER", value: "3" },
    ];
    const expected = {
      type: "BinaryOperation",
      left: {
        type: "Primary",
        dataType: "INTEGER",
        value: "1",
      },
      operator: "PLUS",
      right: {
        type: "BinaryOperation",
        left: {
          type: "Primary",
          dataType: "INTEGER",
          value: "2",
        },
        operator: "MUL",
        right: {
          type: "Primary",
          dataType: "INTEGER",
          value: "3",
        },
      },
    };
    expect(parse(ts)).toEqual(expected);
  });

  it("test_unary_operator", () => {
    const ts: Token[] = [
      { type: "INCREMENT" },
      { type: "INTEGER", value: "1" },
    ];
    const expected = {
      type: "UnaryOperation",
      operator: "INCREMENT",
      operand: {
        type: "Primary",
        dataType: "INTEGER",
        value: "1",
      },
    };
    expect(parse(ts)).toEqual(expected);
  });

  it("test_unary_operator_precedence", () => {
    const ts: Token[] = [
      { type: "INCREMENT" },
      { type: "INTEGER", value: "1" },
      { type: "PLUS" },
      { type: "INTEGER", value: "2" },
    ];
    const expected = {
      type: "BinaryOperation",
      operator: "PLUS",
      left: {
        type: "UnaryOperation",
        operator: "INCREMENT",
        operand: {
          type: "Primary",
          dataType: "INTEGER",
          value: "1",
        },
      },
      right: {
        type: "Primary",
        dataType: "INTEGER",
        value: "2",
      },
    };
    expect(parse(ts)).toEqual(expected);
  });
});
