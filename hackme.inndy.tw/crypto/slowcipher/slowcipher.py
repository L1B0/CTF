#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

import sys

m4x = 0xffffffffffffffff
v7 = 0xDEADBEEF01234567L
v11 = 7
mode, passwd, input = 0,0,0
real_flag = [159, 75, 108, 46]

def trans_v7(x,time):

	for i in range(time):
		x = (0x777777 * x + 12345) & 0x7FFFFFFFFFFFFFFFL 
	return x

def calculate_v7():
	
	global v7,mode,passwd
	for i in range(len(passwd)+1):
		if i == len(passwd):
			password = 0
		else:
			password = ord(passwd[i])
		temp = (777 * password) ^ ( 3333 * ((0x777777 * v7 + 12345) & 0x7FFFFFFFFFFFFFFF)&m4x )
#		print temp,temp>>13,temp^(temp>>13),0x5555555555555555L
		v7 = (temp^(temp>>13)) + 0x5555555555555555L
#		print "v7 == {}".format(v7)
		v7 = trans_v7(v7,password+66)

	print "v7 == {}".format(v7)
	print "calculate_v7 finished!"

def encode_flag():
	
	global v7,v11,mode,passwd,flag
	encode_f = []
	for i in flag:
		
		v16 = ord(i)
		en = v16 
		
		v7 = trans_v7(v7,v11)
		if mode == 1:
			#v11 -> flag 
			v11 = ( (21 * v11 * 0xCCCCCCCCCCCCCCCDL >> 64) >> 3) ^ en
			en = (en^v7)&0xff
			encode_f.append(en)
		else:
			#v11 -> encode_flag
			en = (en^v7)&0xff
			v11 = ( (21 * v11 * 0xCCCCCCCCCCCCCCCDL >> 64) >> 3) ^ en
			encode_f.append(en&0xff)
		print "v11 = {}".format(v11)
	print encode_f
	print "encode_flag = {}".format(''.join(map(chr,encode_f)))

if __name__ == "__main__":

	if len(sys.argv) < 4:
		raise "python exp.py mode password flag"
	mode,passwd,flag = sys.argv[1:]
	mode = 1 if eval(mode)&0xDF!=68 else 0
	flag += '\n'
	calculate_v7()
	encode_flag()
