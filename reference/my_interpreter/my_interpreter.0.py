from builtins import __dict__ as builtins
from dataclasses import dataclass
from opcode import opmap, opname


@dataclass
class MyCodeObject:
    co_code: bytes
    co_consts: tuple


def run_python_bytecode(c: MyCodeObject) -> object:
    """
    Executes the given code object.
    Returns the code's return value.
    """

    # Write interpreter here!


run_python_bytecode(MyCodeObject(
    co_code=b'd\x01}\x00d\x02}\x01|\x00d\x03\x17\x00|\x01\x17\x00}\x02t\x00|\x02\x83\x01\x01\x00d\x00S\x00',
    co_consts=(None, 'Hello', 'World', ' '),
))
