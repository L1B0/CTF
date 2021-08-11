key=[
[0x4a, 0x4a,0x2c,0x71,0x4a, 0x4a,0x2c,0x71,0x4a, 0x4a],
[0x11, 0x11,0xaf,0xbb,0x11, 0x11,0xaf,0xbb,0x11, 0x11],
[0xb8, 0xd3,0xd3,0xb8,0xd3, 0xd3,0xd3,0xb8,0xd3, 0xd3],
[0x37, 0x1b,0xcd,0x1b,0x1b, 0x1b,0xcd,0x1b,0x1b, 0x1b],
[0xb7, 0xa8,0xb7,0xb7,0x02, 0xa8,0xb7,0xb7,0x02, 0xa8],
[0x0b, 0x0b,0x8e,0xee,0xff, 0x0b,0x8e,0xee,0xff, 0x0b],
[0x30, 0x12,0xc9,0x12,0xd7, 0x12,0xc9,0x12,0xd7, 0x12],
[0xe8, 0xe8,0x4b,0x60,0x60, 0xe8,0x4b,0x60,0x60, 0xe8]
]

key2 = [
[0x2c, 0x4a,0x2c,0x4a,0x16, 0x4a,0x2c,0x4a,0x16, 0x4a],
[0x11, 0x11,0x11,0x11,0x1e, 0x11,0x11,0x11,0x1e, 0x11],
[0x9f, 0xd3,0x9f,0xd3,0x9f, 0xd3,0x9f,0xd3,0x9f, 0xd3],
[0x1b, 0x1b,0x1b,0x1b,0x55, 0x1b,0x1b,0x1b,0x55, 0x1b],
[0xb7, 0xbd,0xb7,0xb7,0xb7, 0xbd,0xb7,0xb7,0xb7, 0xbd],
[0x8e, 0x0b,0x8e,0xee,0xff, 0x0b,0x8e,0xee,0xff, 0x0b],
[0x12, 0x12,0x12,0xc9,0xd7, 0x12,0x12,0xc9,0xd7, 0x12],
[0x60, 0xe8,0x60,0x0a,0x4b, 0xe8,0x60,0x0a,0x4b, 0xe8]
]

en_passwd = [0x9a,0x7d,0x72,0x57,0xd5,0x78,0x49,0xe6,0xf2,0x02]


passwd = [ord(i) for i in 'abcefghi']
ori_passwd = passwd[:]

passwd = [0]+passwd+[0]

# 0x254->0x2EA
for i in range(8):

	passwd1 = passwd[:]
        
	passwd[0] = passwd1[2]^key[i][0]
	
	passwd[1] = passwd1[4]^key[i][1]
	passwd[2] = passwd1[7]^key[i][2]
	passwd[3] = passwd1[3]^key[i][3]
	passwd[4] = passwd1[1]^key[i][4]
						
	passwd[5] = passwd1[5]^key[i][5]
	passwd[6] = passwd1[6]^key[i][6]
	passwd[7] = passwd1[2]^key[i][7]
	passwd[8] = passwd1[8]^key[i][8]
						
	passwd[9] = passwd1[3]^key[i][9]
        

	print([hex(k) for k in passwd])

# 0x309->0x314
s = sum(ori_passwd)
a = s&0xff
b = s>>8
print(a,b)
passwd[0] = a
print([hex(k) for k in passwd])

# 0x344->0x3D3
for i in range(8):

	passwd1 = passwd[:]
        
	passwd[0] = passwd1[0]^key2[i][0]
                              
	passwd[1] = passwd1[4]^key2[i][1]
	passwd[2] = passwd1[1]^key2[i][2]
	passwd[3] = passwd1[8]^key2[i][3]
	passwd[4] = passwd1[2]^key2[i][4]
                              
	passwd[5] = passwd1[5]^key2[i][5]
	passwd[6] = passwd1[6]^key2[i][6]
	passwd[7] = passwd1[7]^key2[i][7]
	passwd[8] = passwd1[3]^key2[i][8]
                              
	passwd[9] = passwd1[4]^key2[i][9]
        

	print([hex(k) for k in passwd])

# 0x3d4->0x3d6
passwd[9] = b
print([hex(k) for k in passwd])

en_passwd = [0x7d,0x72,0x75,0xea,0x78,0xa4,0xe6,0xf2]

# 0x3dd->0x3f6
for i in range(1,9):

    # 0x8b0->0x8ba
    j=0x11
    c_flag = 0
    s_t = s
    #s_t = 0x268
    m4x = (9-i)<<16
    
    while 1:
        s_low = ((s_t<<1)&0xffff)+c_flag
        
        j -= 1
        if j == 0:
            s_t = s_t&0xffff0000 +s_low
            break
        
        s_t = (s_t<<1) + c_flag
        
        if s_t >= m4x:
            s_t -= m4x
            c_flag = 0
        else:
            c_flag = 1
       
    b = 8-((s_t>>16)&0xf)
    print(b)
    t = passwd[i]
    passwd[i] = ( (t>>b) ^ ((t<<(8-b))&0xff) )

  
print([hex(k) for k in passwd])