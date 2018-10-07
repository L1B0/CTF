#!/usr/bin/env python2

import random
import string

'''大小写字母前后颠倒'''
def rot13(s):
    return s.translate(string.maketrans(
        string.uppercase[13:] + string.uppercase[:13] +
        string.lowercase[13:] + string.lowercase[:13],
        string.uppercase + string.lowercase))

'''base64编码'''
def base64(s):
    return ''.join(s.decode('base64').split())

def hex(s):
    return s.decode('hex')

'''大写转小写，小写转大写'''
def upsidedown(s):
    return s.translate(string.maketrans(
        string.lowercase + string.uppercase,
        string.uppercase + string.lowercase))

flag = open('flag1.txt','r').read()  # try to recover flag

E = (rot13, base64, hex, upsidedown)

while flag[0:4] != 'FLAG':
    print flag[0]
    flag = E[int(flag[0])](flag[1:])

print flag
