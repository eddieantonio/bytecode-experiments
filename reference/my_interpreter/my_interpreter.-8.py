from builtins import __dict__ as builtins
from dataclasses import dataclass
from opcode import opmap, opname


@dataclass
class MyCodeObject:
    co_code: bytes


def run_python_bytecode(c: MyCodeObject) -> object:
    """
    Executes the given code object.
    Returns the code's return value.
    """

    program_counter = 0
    value_stack = []

    while True:
        # Fetch instruction and argument
        opcode = c.co_code[program_counter]
        arg = c.co_code[program_counter + 1]

        raise NotImplementedError(opname[opcode])

        program_counter += 2

run_python_bytecode(MyCodeObject(
    co_code=b'd\x01}\x00d\x02}\x01|\x00d\x03\x17\x00|\x01\x17\x00}\x02t\x00|\x02\x83\x01\x01\x00d\x00S\x00',
))
