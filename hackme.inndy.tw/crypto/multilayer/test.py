#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

import base64
import binascii
import collections
import hashlib
import os
import random
import string

from Crypto.Util import number

flag = [ord(i) for i in '123456789']

key = number.bytes_to_long(os.urandom(128))

output = []
key1 = []
for i in flag:
	key = (key * 0xc8763 + 9487) % 0x10000000000000000
	output.append((i ^ key) & 0xff)
	key1.append(key)

print output
print flag
print key1
