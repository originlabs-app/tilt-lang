import re
from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: object
    pos: int


def tokenize(code: str):
    token_spec = [
        ("NUMBER", r"\d+"),
        ("STRING", r'"([^"\\]|\\.)*"'),
        ("ARROW", r"->"),
        ("LBRACE", r"\{"),
        ("RBRACE", r"\}"),
        ("LPAREN", r"\("),
        ("RPAREN", r"\)"),
        ("COMMA", r","),
        ("COLON", r":"),
        ("SKIP", r"[ \t]+"),
        ("NEWLINE", r"\n"),
        ("IDENT", r"[A-Za-z_][A-Za-z0-9_]*"),
        ("MISMATCH", r"."),
    ]
    tok_regex = "|".join(f"(?P<{name}>{regex})" for name, regex in token_spec)
    keywords = {"use": "USE", "as": "AS", "fn": "FN", "return": "RETURN"}
    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()
        pos = match.start()
        if kind == "NUMBER":
            yield Token("INT", int(value), pos)
        elif kind == "STRING":
            yield Token("STRING", value[1:-1], pos)
        elif kind == "IDENT":
            yield Token(keywords.get(value, "IDENT"), value, pos)
        elif kind in {"SKIP", "NEWLINE"}:
            continue
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character {value!r} at position {pos}")
        else:
            yield Token(kind, value, pos)
    yield Token("EOF", "", len(code))
