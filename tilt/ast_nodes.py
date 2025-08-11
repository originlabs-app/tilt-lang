from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Union


@dataclass
class Program:
    body: List[object]


@dataclass
class UseStmt:
    module: str
    alias: Optional[str] = None


@dataclass
class Param:
    name: str
    type: str


@dataclass
class FnDecl:
    name: str
    params: List[Param]
    return_type: Optional[str]
    body: List[object]


@dataclass
class ReturnStmt:
    value: object


@dataclass
class Identifier:
    name: str


@dataclass
class Literal:
    value: Union[int, str]


@dataclass
class CallExpr:
    callee: Identifier
    args: List[object]
