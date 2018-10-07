#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

byte_406920 = [47,115,155,195,235,999]
byte_460811F = []

def func1():
	v4 = 0
	v5 = 0x2f
	i = 0
	while v4 < 256:
	
		v7 = 1 if v5 < v4 else 0
		v4 += 1
		i += v7
		byte_460811F.append(i)
		v5 = byte_406920[i] 
	
	print byte_460811F

if __name__ == "__main__":
	func1()
