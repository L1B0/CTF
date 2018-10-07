#!/usr/bin/env python

from Crypto.Cipher import AES
import string
import random
import sys
import signal

key = "XXXXXXXXXXXXXXXX"
flag = "FLAG{..........................}" # Not real flag ...
iv = ''.join(random.choice(string.hexdigits) for _ in range(16))

signal.alarm(60)

def encrypt(p):
    return AES.new(key, AES.MODE_OFB, iv).encrypt(p)


print \
"""
    _    ___ ____ _____   ____   _    ____ ____   ____ ___  ____  _____
   / \  |_ _/ ___|___ /  |  _ \ / \  / ___/ ___| / ___/ _ \|  _ \| ____|
  / _ \  | |\___ \ |_ \  | |_) / _ \ \___ \___ \| |  | | | | | | |  _|
 / ___ \ | | ___) |__) | |  __/ ___ \ ___) |__) | |__| |_| | |_| | |___
/_/   \_\___|____/____/  |_| /_/   \_\____/____/ \____\___/|____/|_____|
"""

print "Try to decode the cipher:"
print encrypt(flag).encode("hex")
print "===================================================================="
sys.stdout.flush()


a = [[0]*26 for i in range(26)]

while True:
    print "Calcuate the passcode...(Press any key to continue)"
    sys.stdout.flush()
    b = raw_input()
    if b == 'q':
	    break
    p = 'abcdefghijklm'+''.join(random.choice(string.lowercase) for _ in range(3))
    print p
    print encrypt(p).encode('hex')
    a[0][ord(p[-1])-ord('a')] = encrypt(p).encode("hex")[-2:]
    a[1][ord(p[-2])-ord('a')] = encrypt(p).encode("hex")[-4:-2]
    a[2][ord(p[-3])-ord('a')] = encrypt(p).encode("hex")[-6:-4]
    sys.stdout.flush()
print a[0]
print a[1]
print a[2]
