data = [0x3F, 0x01, 0x20, 0x4A, 0xE9, 0x67, 0xCB, 0xD8, 0x40, 0xF3, 
  0x3F, 0x01, 0x20, 0x4A, 0xE9, 0x67, 0xCB, 0xD8, 0x40, 0x50, 
  0x70, 0x20, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
  0x00]

v23 = [
  0,
  0,
  184,
  92,
  139,
  107,
  66,
  184,
  56,
  237,
  219,
  91,
  129,
  41,
  160,
  126,
  80,
  140,
  27,
  134,
  245,
  2,
  85,
  33,
  12,
  14,
  242,
  0
]

i = 0
while True:
	
	if i == 25:
		break
	
	i += 5
	v23[i] ^= ((data[i-1]-12)&0xff)
	v23[i] ^= ((data[i-5]-12)&0xff)
	v23[i+1] ^= ((data[i-4]-12)&0xff)
	v23[i+1] ^= ((data[i-3]-12)&0xff)
	v23[i+2] ^= ((data[i-2]-12)&0xff)

for i in range(25):
	v23[i+2] = i + (v23[i+2] ^ 0xf)

print v23[2:27]