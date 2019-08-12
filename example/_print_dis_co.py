#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from greetings import greet
import dis

co = greet.__code__
dis.dis(greet)
print('co_code =', co.co_code)
print('co_nclocals =', co.co_nlocals)
print('co_consts =', co.co_consts)
print('co_conames =', co.co_names)
