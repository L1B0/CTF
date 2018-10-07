#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'
import base64
from string import printable
from z3 import *

cipher = "25-Q44E233=,>E-M34=,,$LS5VEQ45)M2S-),7-$/3T \x00"
print len(cipher)

def decode_level1(s):
	if len(s)%4 != 0:
		return base64.b64decode(s[:len(s)-len(s)%4])

def decode_level2(s):

	s1 = ''
	for i in s:
		j = ord(i)
		for k in range(256):
			l = 0
			if (k <= 0x40 or k > 0x5a):
				if (k <= 0x60 or k > 0x7a):
					l = k
				else:
					l = (k-0x54)%26 + 0x61 
			else:
				l = (k-0x34)%26 + 0x41 
			if l == j:
				s1 += chr(k)
				break

	print len(s),len(s1)
	return s1 

def decode_level3(cipher):
	
	ss = ""
	
	for i in range(11):
		
		s = Solver()
		a1,a2,a3 = [ BitVec('a'+str(j),16) for j in range(1,4) ]
		for j in range(1,4):
			s.add( And( eval('a'+str(j)) > 0, eval('a'+str(j)) < 256 ) )

		s.add( (a1>>2) + 32 == ord(cipher[4*i]) )
		s.add( (( ((16*a1)&0x30) + 32 ) | (a2 >> 4)) == ord(cipher[4*i+1]) )
		s.add( ((((4*a2)&0x3c) +32) | (a3 >> 6) ) == ord(cipher[4*i+2]) )
		s.add( (a3&0x3f) +32 == ord(cipher[4*i+3]) )
		
		print s.check()
		if s.check() == sat:

			print s.model()
			
			ss += chr(s.model()[a1].as_long())
			ss += chr(s.model()[a2].as_long())
			ss += chr(s.model()[a3].as_long())
			print ss

	print ss 
	return ss 


if __name__ == "__main__":
	
	flag2 = decode_level3(cipher)
	flag1 = decode_level2(flag2)
	print flag1
	flag = decode_level1(flag1)

	print flag 
