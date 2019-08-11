from dataclasses import dataclass

@dataclass
class MyCodeObject:
    co_code: bytes
    co_consts: tuple
    co_nlocals: int

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

        if opcode == 0x64:  # LOAD_CONST
            stack.append(c.co_consts[arg])
        elif opcode == 0x7d:  # STORE_FAST
            value = stack.pop()
            local_variables[arg] = value
        elif opcode == 0x7c:  # LOAD_FAST
            value = local_variables[arg]
            stack.append(value)
        else:
            raise NotImplementedError(hex(opcode))
        print("stack:", stack)
        print("locals:", local_variables)
        print()

        pc += 2

run_python_bytecode(MyCodeObject(
    co_code=b'd\x01}\x00d\x02}\x01|\x00d\x03\x17\x00|\x01\x17\x00}\x02t\x00|\x02\x83\x01\x01\x00d\x00S\x00',
    co_consts=(None, 'Hello', 'World', ' '),
    co_nlocals=3,

))
