#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from dis import dis
from greetings import greet
import marshal
import types

dis(greet)

with open('greetings.py') as source_code:
    code = compile(source_code.read(), 'greetings.py', 'exec')

# Marshalling code:
# https://github.com/python/cpython/blob/b9a0376b0dedf16a2f82fa43d851119d1f7a2707/Python/marshal.c#L529-L548
with open('module.bin', 'wb') as bytecode_file:
    marshal.dump(code, bytecode_file)

with open('./__pycache__/greetings.cpython-37.pyc', 'rb') as pyc:
    # Ignore the first 16 bytes. Dunno what's up with that.
    header = pyc.read(0x10)
    code_object = marshal.load(pyc)

fn_code = code_object.co_consts[0]
assert isinstance(fn_code, types.CodeType)
