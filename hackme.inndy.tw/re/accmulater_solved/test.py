import ctypes

dll = ctypes.CDLL('/usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0')
s = 'flag{123456798}'
a=0
print dll.SHA512(s,len(s),a)
print s
