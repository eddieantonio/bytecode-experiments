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

    pc = 0  # pc = program counter
    stack = []
    local_variables = [None] * c.co_nlocals

    while pc < len(c.co_code):
        opcode = c.co_code[pc]
        arg = c.co_code[pc + 1]

        if opcode == opmap['LOAD_CONST']:
            stack.append(c.co_consts[arg])
        elif opcode == opmap['STORE_FAST']:
            value = stack.pop()
            local_variables[arg] = value
        elif opcode == opmap['LOAD_FAST']:
            value = local_variables[arg]
            stack.append(value)
        elif opcode == opmap['BINARY_ADD']:
            rhs = stack.pop()
            lhs = stack.pop()
            value = lhs + rhs
            stack.append(value)
        elif opcode == opmap['LOAD_GLOBAL']:
            name = c.co_names[arg]
            if name in globals():
                value = globals()[name]
            elif name in __builtins__.__dict__:
                value = __builtins__.__dict__[name]
            else:
                raise NameError(f'name {name} is not defined')
            stack.append(value)
        elif opcode == opmap['CALL_FUNCTION']:
            argv = []
            for _ in range(arg):
                argv.append(stack.pop())
            assert len(stack) >= 1
            function = stack.pop()
            value = function(*argv)
            stack.append(value)
        elif opcode == opmap['POP_TOP']:
            stack.pop()
        elif opcode == opmap['RETURN_VALUE']:
            return stack.pop()
        else:
            raise NotImplementedError(opname[opcode])

        pc += 2

run_python_bytecode(MyCodeObject(
    co_code=b'd\x01}\x00d\x02}\x01|\x00d\x03\x17\x00|\x01\x17\x00}\x02t\x00|\x02\x83\x01\x01\x00d\x00S\x00',
    co_consts=(None, 'Hello', 'World', ' '),
    co_nlocals=3,
    co_names=('print',)
))
