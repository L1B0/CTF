a = [0x8F,0xAA,0x85,0xA0,0x48,0xAC,0x40,0x95,0xB6,0x16,0xBE,0x40,0xB4,0x16,0x97,0xB1,0xBE,0xBC,0x16,0xB1,0xBC,0x16,0x9D,0x95,0xBC,0x41,0x16,0x36,0x42,0x95,0x95,0x16,0x40,0xB1,0xBE,0xB2,0x16,0x36,0x42,0x3D,0x3D,0x49]
flag = ''
for i in range(len(a)):
         flag += chr( (((a[i]&0xAA)>>1) | (2*(a[i]&0x55))) - 9 )
print(flag)
