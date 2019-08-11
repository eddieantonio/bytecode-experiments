# Code flags used here:
CO_OPTIMIZED = 0x0001
CO_NEWLOCALS = 0x0002
CO_NOFREE    = 0x0040

# See: https://github.com/python/cpython/blob/3.7/Lib/py_compile.py
# See: https://www.python.org/dev/peps/pep-3147/
# See: https://www.python.org/dev/peps/pep-0488/
# See: https://github.com/python/cpython/blob/c48d606adcef395e59fd555496c42203b01dd3e8/Lib/importlib/_bootstrap_external.py#L252-L260

# == .pyc header ==
# See: https://github.com/python/cpython/blob/3.7/Lib/importlib/_bootstrap_external.py
_RAW_MAGIC_NUMBER = 3394  # Python 3.7b5
# 00000000: 420d 0d0a                                B...
#                     (timestamp .pyc)
#                       mtime = 2019-08-10T03:28:27+00:00
#                           source_size = 171
# 00000004:           0000 0000 db39 4e5d ab00 0000      .....9N]....

# Reference:
# https://github.com/python/cpython/blob/3.7/Include/code.h#L21-L51
# https://github.com/python/cpython/blob/3.7/Python/marshal.c#L549-L565

# == Code object [module] ==
#
#           𝚌
# argscount = 0
#      kwonlyargcount = 0
#                       nlocals = 0
#                               stacksize = 2
# 00000010: e300 0000 0000 0000 0000 0000 0002 0000  ................
#  co_flags = CO_NOFREE
#                       𝚜  12
#   0000: 6400 LOAD_CONST       0x00 ('greet')
#   0002: 6401 LOAD_CONST       0x01 (<function greet()>)
#   0004: 8400 MAKE_FUNCTION    0x00 <no flags set>
#   0006: 5a00 STORE_NAME       0x00 (greet)
#   0008: 6400 LOAD_CONST       0x02 (None)
# 00000020: 0040 0000 0073 0c00 0000 6400 6401 8400  .@...s....d.d...
# 00000030: 5a00 6402 5300 2903                      Z.d.S.).

# == Code object [greet()] ==
co_argcount =                     0
co_kwonlyargcount =                              0
# 00000038:                     6300 0000 0000 0000          c.......
co_nlocals =  3
co_stacksize =          2
# 00000040:   03 0000 0002 0000 0043 0000 00          ........C...
co_flags = CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE
# 00000040:                       43 0000 00                  C...
#

# == bytecode for <function greet()> ==
#                               's'=TYPE_BYTES len=32 bytes
# 0000004d:                                 73 2000               s .
# 00000050: 0000                                     ..
co_code     = (b'd\x01}\x00d\x02}\x01|\x00d\x03\x17'
          b'\x00|\x01\x17\x00}\x02t\x00|\x02\x83\x01\x01\x00d\x00'
          b'S\x00')
# 00000052:      6401 7d00 6402 7d01 7c00 6403 1700    d.}.d.}.|.d...
# 00000060: 7c01 1700 7d02 7400 7c02 8301 0100 6400  |...}.t.|.....d.
# 00000070: 5300                                     S.

# == constant used ==
#                𝚜 𝟒  𝙽 𝚉  𝟱              𝚉 𝟱
co_consts =           (None, 'Hello', 'World',
# 00000072:      2904 4e5a 0548 656c 6c6f 5a05 576f    ).NZ.HelloZ.Wo
# 00000080: 726c 64                                  rld
#                  𝚣. 𝟏
                        ' ')
# 00000083:        fa 0120                                ..

# == names used ==
#                          𝚜 𝟏  𝚉.𝟱
co_names =                          ('print',)
# 00000086:                2901 da05 7072 696e 74          )...print

# == local variable names ==
#         𝚜 𝟑 𝚣  𝟖         𝚣 𝟖         𝚣  𝟗
co_varnames =    ('greeting',              'recipient',
# 0000008f:                                      29                 )
# 00000090: 035a 0867 7265 6574 696e 675a 0972 6563  .Z.greetingZ.rec
                               'sentence')
# 000000a0: 6970 6965 6e74 5a08 7365 6e74 656e 6365  ipientZ.sentence

# == cell variable names ==
#           𝚜. 𝟢
co_cellvars = ()
# 000000b0: a900

# == where it was loaded from ==
#                𝚛 𝟑         𝚣. 𝟏𝟒
co_filename =                    './greetings.py'
# 000000b0:      7203 0000 00fa 0e2e 2f67 7265 6574  ..r......./greet
# 000000c0: 696e 6773 2e70 79

# == name, for reference ==
#                            𝚉  𝟓
co_name =                         'greet'
# 000000c7:                  da 0567 7265 6574              ..greet


# == first source line number ==
#        𝟒
co_firstlineno = 4
# 000000c7:                                    0400                ..
# 000000d0: 0000

# == encoding addr<->lineno mapping ==
co_lnotab =                b'\x00\x01\x04\x01\x04\x01\x0c\x02'
# 000000d2:      7308 0000 0000 0104 0104 010c 02    ..s............
# 000000d2:                                      72                 r
# 000000e0: 0500 0000

# == stuff AFTER the code object we care about! ==
# == probably inside the module's constant table ==
# 000000e4:           4e29 0172 0500 0000 7203 0000      N).r....r...
# 000000f0: 0072 0300 0000 7203 0000 0072 0400 0000  .r....r....r....
# 00000100: da08 3c6d 6f64 756c 653e 0400 0000 7300  ..<module>....s.
# 00000110: 0000 00                                  ...
