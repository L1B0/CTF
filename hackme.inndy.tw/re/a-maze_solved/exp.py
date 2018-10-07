#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'
from pwn import *
from z3 import *

m = open("map",'r').read()
print len(m)

'''
l = []
ll = []
lll = []

for i in range(len(m)):
	if m[i:i+4] == '\xff\xff\xff\xff':
		l.append(i)
print "len(l) == {}".format(len(l))

def lev1():
	for i in l:
		for j in range(2009):
			for k in range(0x7f):
				if i == (j<<9)+4*k:
					print "{} == {}<<9+4*{}".format(i,j,k)
					ll.append(j)


def lev2():
	for i in range(len(m)):
		if m[i:i+4] == '\xd8\x07\x00\x00':
			print i
			lll.append(i)
	for i in lll:
		for j in range(2000):
			for k in range(0x7f):
				if i == 1006068 and j == 1964 and k == 0x7d:
					print i==(j<<9)+4*k
				if i == (j<<9)+4*k:
					print "{} == {}<<9+4*{}".format(i,j,k)
	
'''				

def get_flag():
	flag = ''
	v2 = 0xffffffff
	while(1):
		for j in range(3000):
			for k in range(0x7f):
				pos = (j<<9)+4*k
				if v2 == u32(m[pos:pos+4]):
					print "{} == {}<<9+4*{}".format(pos,j,k)
					v2 = j
					flag += chr(k)
					print flag
					break
			if v2 == 0:
				break
		if v2 == 0:
			break
	print flag[::-1]


if __name__ == "__main__":
#lev1()
#lev2()
	get_flag()
