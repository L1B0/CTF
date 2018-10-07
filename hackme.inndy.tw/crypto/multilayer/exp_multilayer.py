#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'
#https://quipqiup.com/

import base64
import binascii
import collections
import hashlib
import os
import random
import string
import re
from libnum import s2n,n2s
import gmpy2
from Crypto.Util import number

cipher = open('encrypted','rb').read()
n=0x80dd2dec6684d43bd8f2115c88717386b2053bdb554a12d52840380af48088b7f1f71c3d3840ef4615af318bbe261d2d2d90616c0d2dcb6414e05c706f2b6d700ed98128048a2b79f57d2c6476add369ec96fb0fed936506d9aee4da5d36aaa97f117b082924c0638923e4367f250cc6cd23918702d98c5359bbb6bad2bef741c65362ad40355fd2edb35248256413d0ee576e7a351f17b9a5a3a7eebbbb2b22f27c342ef6dcaf1396085a105cf5e8b9bbf80e002053347fd9db6e83dc63599b1e1e5a81f7f2e4e2473bc2d14d040c9c6e6f62b9027853c7550a10df49c3a786962c9e9d5b95551a95077d0bd354b88ef31c5625e21edf98f721504f73e1b867
e=0xcf98d5

flag_counter = {' ': 14, 'O': 6, 'A': 5, 'U': 4, 'I': 4, 'T': 4, 'N': 3, 'D': 3, 'E': 3, 'L': 3, 'H': 3, 'Y': 3, 'R': 3, 'G': 2, 'C': 2, 'F': 2, 'W': 2, '.': 1, '}': 1, 'B': 1, 'V': 1, 'Q': 1, 'P': 1, 'X': 1, 'M': 1, '\n': 1, '{': 1, 'K': 1, 'J': 1, 'S': 1, 'Z': 1}

flag = "FLAG{"

def xor(a, b):
    return s2n(''.join([chr(ord(i) ^ ord(j)) for i, j in zip(a, b)]))

def rsa_encrypt(m):

	return pow(s2n(m),e,n)

def burp_m(c):
	
	zidian = "0123456789abcdef"

	for i in zidian:
		for j in zidian:
			for k in zidian:
				for l in zidian:
					m1 = i+j+k+l
					if rsa_encrypt(m1) == c:
						return m1
	return 'false'

def decode_layer4():
	
	cipher_layer4 = ""
	for i,j in enumerate(cipher):
		if cipher[i:i+4] == "eH/V":
			cipher_layer4 = cipher[i:]
			break
	#print cipher_layer4
	cipher_layer4 = base64.b64decode(cipher_layer4)
	print type(cipher_layer4),len(cipher_layer4)
	
	cipher4 = []
	for i in range(41):
		c = ''
		for j in range(256):
			c += cipher_layer4[i*256+j]
		cipher4.append(c)
	#print len(cipher4),cipher4
	
	cipher3 = ""
	for i in range(1,41):
		a = xor(cipher4[i-1],cipher4[i])
		print "Try {} -> {}".format(i,a)
		b = burp_m(a)
		if b != 'false':
			print b
			cipher3 += b
	print cipher3

def layer3_and_layer2(text,key):

	cipher_3= ""
	for i in text:
		key = (key * 0xc8763 + 9487)&0xff
		cipher_3 += chr(ord(i)^key)

	cipher_2 = ""
	key_layer2 = gmpy2.invert(17,251)
	print "key_layer2 -> {}".format(key_layer2)
	for i in cipher_3:
		cipher_2 += chr( (ord(i)*192) % 251 )
	return cipher_2 

def decode_layer3_layer2(cipher3):

	cipher1 = []
	'''
	num = 0
	flag_str = ""
	print len(flag_counter)
	for i,j in flag_counter.items():
		num += j
		flag_str += i
	flag_str = "".join((lambda x:(x.sort(),x)[1])(list(flag_str)))

	print "flag_len -> {}".format(num)
	'''

	for i in range(256):
		temp = layer3_and_layer2(cipher3,i)
		cipher1.append(temp)
	print cipher1

if __name__ == "__main__":
	
	print rsa_encrypt('1234')
#	decode_layer4()
	print "layer4 clear!"
	cipher3 = binascii.unhexlify("58cf2de2cf8e72d8c28b1925e6962d51a3630af38a84923462d397d60665995fa1313e4444890cba0e201a43fa9ee2877c115e64a4e9116362fd4c34c68fc50c6edca071d795ee295ece1d3fd46efd0d")
	decode_layer3_layer2(cipher3)

	
