#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# based on: https://github.com/python/cpython/blob/92c7e30adf5c81a54d6e5e555a6bdfaa60157a0d/Include/code.h#L22-L69

from enum import IntEnum


class Flags(IntEnum):
    CO_OPTIMIZED            = 0x0001
    CO_NEWLOCALS            = 0x0002
    CO_VARARGS              = 0x0004
    CO_VARKEYWORDS          = 0x0008
    CO_NESTED               = 0x0010
    CO_GENERATOR            = 0x0020
    # CO_NOFREE flag is set if there are no free (global) or cell variables (closures)
    CO_NOFREE               = 0x0040
    CO_COROUTINE            = 0x0080
    CO_ITERABLE_COROUTINE   = 0x0100
    CO_ASYNC_GENERATOR      = 0x0200


class PyCodeObject:
    co_argcount: int        # how many arguments, except *args
    co_posonlyargcount: int # how many positional ONLY args
    co_kwownlyargcount: int # how many keyword-only arguments
    co_nlocals: int         # how many local variables
    co_stacksize: int       # how many entries needed for evaluation stack
    co_flags: Flags         # CO_...
    co_firstlineno: int     # first source line number
    co_code: bytes          # instruction opcodes
    co_consts: list         # constants used (any)
    co_names: list          # names used (strings)
    co_varnames: tuple      # local variable names (strings)
    co_freevars: tuple      # free variable names (strings)
    # ???
    co_cellvars: tuple      # cell variable names (strings

    # ???
    co_cell2arg: int        # maps cell vars which are arguments
    co_filename: str        # where it was loaded from
    co_name: str            # name
    co_lnotab: bytes        # address<->line-number mapping
    co_zombieframe: object  # for optimization only
    co_weakreflist: list    # to support weakrefs to code objects
    co_extra: object        # extra stuff

    # caching stuff
