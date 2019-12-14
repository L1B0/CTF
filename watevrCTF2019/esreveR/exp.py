a2 = 0x427d8616 
a3 = 0xc2 
a4 = 0xffffffffc7f2682d 
a5 = 0x5cbfb3d5 
a6 = 0xffffffff9a1391c2 

v6 = a3 ^ 0x98
v7 = v6
v8 = a3
v8 = a3 ^ 0xA7

flag = []
flag.append((a6 ^ 0xFFFFFFFF9A1391B5)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391A3)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B6)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391A7)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B4)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B0)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B9)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391A7)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B1)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B0)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391A7)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B4)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391A7)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B0)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A13919D)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B0)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391A7)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B4)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391A7)&0xff)
flag.append((a6 ^ 0xFFFFFFFF9A1391B0)&0xff)

flag.append((a5 ^ 0x5CBFB3A6)&0xff)
flag.append((a5 ^ 0x5CBFB3B0)&0xff)
flag.append((a5 ^ 0x5CBFB3B1)&0xff)
flag.append((a5 ^ 0x5CBFB38A)&0xff)
flag.append((a5 ^ 0x5CBFB3AC)&0xff)
flag.append((a5 ^ 0x5CBFB3BA)&0xff)
flag.append((a5 ^ 0x5CBFB3A0)&0xff)
flag.append((a5 ^ 0x5CBFB3A1)&0xff)
flag.append((a5 ^ 0x5CBFB3A0)&0xff)
flag.append((a5 ^ 0x5CBFB3B7)&0xff)
flag.append((a5 ^ 0x5CBFB3B0)&0xff)
flag.append((a5 ^ 0x5CBFB3FB)&0xff)
flag.append((a5 ^ 0x5CBFB3B6)&0xff)
flag.append((a5 ^ 0x5CBFB3BA)&0xff)
flag.append((a5 ^ 0x5CBFB3B8)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26802)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F2685A)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F2684C)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26859)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F2684E)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26845)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26812)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F2685B)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26810)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26864)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26815)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26844)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26847)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F2684F)&0xff)
flag.append((a4 ^ 0xFFFFFFFFC7F26819)&0xff)
flag.append((v7)&0xff)
flag.append((v8)&0xff)
flag.append((a2)&0xff)
flag.append((a2 ^ 0x427D8623)&0xff)
flag.append((a2 ^ 0x427D8653)&0xff)
flag.append((a2 ^ 0x427D866B)&0xff)

print flag,a2&0xff
print ''.join(map(chr,flag))