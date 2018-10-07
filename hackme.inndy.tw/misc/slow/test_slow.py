#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
import time 

flag = 'FLAG{'
string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+_'

while True:
	for i in string:
		io = remote('hackme.inndy.tw',7708)
		io.recvuntil("What is your flag?")
		a = time.time()
		io.sendline(flag+i+'}')
		s = io.recvline()
		b = time.time()
		print "now_char = {}  now_time = {}".format(i,math.floor(b-a))

