#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'
from pwn import *
context.log_level = 'debug'
a0 = [
'%^Jv',
'/JTl',
'/JTt',
'J/Tl',
'J/Tt',
'^%Jv'	
]
a4 = [
'C=&'
]

def is_Prime(n):
	if n <= 2:
		return 1
	for i in range(2,n):
		if n%i == 0:
			return 0
	return 1

	 
def get_0123():

	for i in range(33,127):
		for j in range(33,127):
			for k in range(33,127):
				if not(i*j == 3478 and (j^i)^k == 49):
					continue
				else:
					for l in range(k+1,127):
						if (l**2)%256 == (k**2)%256:
							s = chr(i)+chr(j)+chr(k)+chr(l)
							print s

def get_456():
	for i in range(33,127):
		for j in range(33,127):
			if (j-42) > 0 and is_Prime(i) and is_Prime(j) and is_Prime(j-42) and i^j == 126:
				s = chr(i)+chr(j)+chr(2*(j-42))
				print s

if __name__ == "__main__":
	
#get_0123()
#get_456()
	for i in a0:
		for j in a4:
			for k in [48,52,56]:
				a7 = k
				#*(_BYTE *)(a3 + 8) == (a1 ^ *(_BYTE *)(a3 + 7)); a1 = 0x12 by debug
				a8 = a7^0x12 
				a9 = 2*a8
				a100 =  (a9+1)*(a9)/2 
				#burte a10
				for l in range(33,127):
					s = i+j+chr(a7)+chr(a8)+chr(a9)+chr(l)
					print s
				
					io = process('./GuessTheString')
					io.recvline()
					io.sendline(s)
					io.recvline()
					io.close()

				
				
