from builtins import __dict__ as builtins
from dataclasses import dataclass
from opcode import opmap, opname


@dataclass
class MyCodeObject:
    co_code: bytes
    co_consts: tuple
    co_nlocals: int
    co_names: tuple


def run_python_bytecode(c: MyCodeObject) -> object:
    """
    Executes the given code object.
    Returns the code's return value.
    """

    program_counter = 0
    value_stack = []
    local_variables = [None] * c.co_nlocals

    while True:
        # Fetch instruction and argument
        opcode = c.co_code[program_counter]
        arg = c.co_code[program_counter + 1]

        if opcode == opmap['LOAD_CONST']:
            value = c.co_consts[arg]
            value_stack.append(value)
        elif opcode == opmap['STORE_FAST']:
            value = value_stack.pop()
            local_variables[arg] = value
        elif opcode == opmap['LOAD_FAST']:
            value = local_variables[arg]
            value_stack.append(value)
        elif opcode == opmap['BINARY_ADD']:
            rhs = value_stack.pop()
            lhs = value_stack.pop()
            value = lhs + rhs
            value_stack.append(value)
        elif opcode == opmap['LOAD_GLOBAL']:
            name = c.co_names[arg]
            if name in globals():
                value = globals()[name]
            elif name in builtins:
                value = builtins[name]
            else:
                raise NameError(f'name {name} is not defined')
            value_stack.append(value)
        elif opcode == opmap['CALL_FUNCTION']:
            args = []
            for _ in range(arg):
                args.append(value_stack.pop())
            function = value_stack.pop()
            value = function(*args)
            value_stack.append(value)
        elif opcode == opmap['POP_TOP']:
            value_stack.pop()
        else:
            raise NotImplementedError(opname[opcode])

        program_counter += 2

run_python_bytecode(MyCodeObject(
    co_code=b'd\x01}\x00d\x02}\x01|\x00d\x03\x17\x00|\x01\x17\x00}\x02t\x00|\x02\x83\x01\x01\x00d\x00S\x00',
    co_consts=(None, 'Hello', 'World', ' '),
    co_nlocals=3,
    co_names=('print',)
))
