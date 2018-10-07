#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

import string
a = string.lowercase+string.uppercase+'0123456789'
b = string.lowercase
c = string.uppercase
d = '0123456789'
num = 0
zidian = ''

def create(a):
	global zidian,num
	
	for i in a:
		for j in a:
			for k in a:
				for l in a:
					num += 1
					print num
					zidian += (i+j+k+l+'\n')
	
	
	print "finished"

create(b)
create(c)
create(d)

with open("zidian.txt",'w') as f:
	f.write(zidian)




