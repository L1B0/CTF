#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
from sys import *

encode_flag = []
ciphertext = [ [0]*26 for i in range(200) ]
num = 0
key = []

isLower = lambda x: x >= ord('a') and x <= ord('z')
xor = lambda x,y: ''.join(map(chr,[x[i]^y[i] for i in range(32)]))

def remote_get_cipher():

	global encode_flag,ciphertext,num
	io = remote("hackme.inndy.tw",7700)

	io.recvuntil("cipher:\n")
	encode_flag = io.recvline()[:64].decode('hex')
	encode_flag = map(ord,encode_flag)

	while(num < 100):
		print num
		io.recvuntil("(Press any key to continue)\n")
		io.sendline("\n")
		t = io.recvline()[:64].decode('hex')
		ciphertext[num] = map(ord,t)
		num += 1
	io.interactive()

def local_get_cipher():

	global encode_flag,ciphertext,num
	
	a = open("cipher.txt",'r').readlines()
	encode_flag = a[0][:64].decode('hex')
	encode_flag = map(ord,encode_flag)
	
	for i in range(1,len(a)):
		if len(a[i]) != 65:
			continue
		t = a[i][:64].decode('hex')
		ciphertext[num] = map(ord,t)
		num += 1

def guess_key():

	global encode_flag,ciphertext,key,num

	for i in range(32):
		flag = True
		for j in range(255):
			flag=True
			for k in range(num):
				flag = isLower(ciphertext[k][i]^j) 
				if flag == False:
					break
			if flag == True:
				print "FInd {}!".format(i)
				key.append(j)
				break
		
	print xor(key,encode_flag)

if __name__ == "__main__":
	
	local_get_cipher()
#	print encode_flag,ciphertext
	guess_key()
