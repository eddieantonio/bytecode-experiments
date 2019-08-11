from dataclasses import dataclass

@dataclass
class MyCodeObject:
    co_code: bytes

def run_python_bytecode(c: MyCodeObject) -> object:
    """
    Executes the given code object.
    Returns the code's return value.
    """

    pc = 0  # pc = program counter
    
    while pc < len(c.co_code):
        opcode = c.co_code[pc]
        arg = c.co_code[pc + 1]

        if opcode == ...:
            pass
        else:
            raise NotImplementedError(hex(opcode))

        pc += 2

run_python_bytecode(MyCodeObject(
    co_code=b'd\x01}\x00d\x02}\x01|\x00d\x03\x17\x00|\x01\x17\x00}\x02t\x00|\x02\x83\x01\x01\x00d\x00S\x00'
))
