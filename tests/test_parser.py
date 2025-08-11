import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from tilt.parser import parse_program
from tilt.ast_nodes import FnDecl, ReturnStmt, UseStmt, Literal


def test_parse_use_and_fn():
    source = """
    use db
    fn main() { return 42 }
    """
    program = parse_program(source)
    assert len(program.body) == 2
    assert isinstance(program.body[0], UseStmt)
    assert program.body[0].module == "db"
    fn = program.body[1]
    assert isinstance(fn, FnDecl)
    assert fn.name == "main"
    assert isinstance(fn.body[0], ReturnStmt)
    assert isinstance(fn.body[0].value, Literal)
    assert fn.body[0].value.value == 42
