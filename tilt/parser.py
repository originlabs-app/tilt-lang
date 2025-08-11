from __future__ import annotations

from typing import List

from .ast_nodes import (
    CallExpr,
    FnDecl,
    Identifier,
    Literal,
    Param,
    Program,
    ReturnStmt,
    UseStmt,
)
from .lexer import Token, tokenize


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def current(self) -> Token:
        return self.tokens[self.pos]

    def consume(self, expected: str) -> Token:
        token = self.current()
        if token.type != expected:
            raise SyntaxError(f"Expected {expected} but got {token.type}")
        self.pos += 1
        return token

    def accept(self, token_type: str) -> Token | None:
        if self.current().type == token_type:
            return self.consume(token_type)
        return None

    def parse_program(self) -> Program:
        body = []
        while self.current().type != "EOF":
            tok = self.current()
            if tok.type == "USE":
                body.append(self.parse_use())
            elif tok.type == "FN":
                body.append(self.parse_fn())
            else:
                raise SyntaxError(f"Unexpected token {tok.type}")
        return Program(body)

    def parse_use(self) -> UseStmt:
        self.consume("USE")
        module = self.consume("IDENT").value
        alias = None
        if self.accept("AS"):
            alias = self.consume("IDENT").value
        return UseStmt(module, alias)

    def parse_fn(self) -> FnDecl:
        self.consume("FN")
        name = self.consume("IDENT").value
        self.consume("LPAREN")
        params = []
        if self.current().type != "RPAREN":
            params = self.parse_params()
        self.consume("RPAREN")
        return_type = None
        if self.accept("ARROW"):
            return_type = self.consume("IDENT").value
        body = self.parse_block()
        return FnDecl(name, params, return_type, body)

    def parse_params(self) -> List[Param]:
        params = []
        while True:
            name = self.consume("IDENT").value
            self.consume("COLON")
            typ = self.consume("IDENT").value
            params.append(Param(name, typ))
            if not self.accept("COMMA"):
                break
        return params

    def parse_block(self) -> List[object]:
        self.consume("LBRACE")
        stmts = []
        while self.current().type != "RBRACE":
            stmts.append(self.parse_stmt())
        self.consume("RBRACE")
        return stmts

    def parse_stmt(self) -> object:
        if self.current().type == "RETURN":
            return self.parse_return()
        raise SyntaxError(f"Unexpected statement token {self.current().type}")

    def parse_return(self) -> ReturnStmt:
        self.consume("RETURN")
        value = self.parse_expr()
        return ReturnStmt(value)

    def parse_expr(self) -> object:
        token = self.current()
        if token.type == "INT":
            self.consume("INT")
            return Literal(token.value)
        if token.type == "STRING":
            self.consume("STRING")
            return Literal(token.value)
        if token.type == "IDENT":
            ident = Identifier(self.consume("IDENT").value)
            if self.accept("LPAREN"):
                args = []
                if self.current().type != "RPAREN":
                    args = self.parse_args()
                self.consume("RPAREN")
                return CallExpr(ident, args)
            return ident
        raise SyntaxError(f"Unexpected expression token {token.type}")

    def parse_args(self) -> List[object]:
        args = [self.parse_expr()]
        while self.accept("COMMA"):
            args.append(self.parse_expr())
        return args


def parse_program(source: str) -> Program:
    tokens = list(tokenize(source))
    parser = Parser(tokens)
    return parser.parse_program()
