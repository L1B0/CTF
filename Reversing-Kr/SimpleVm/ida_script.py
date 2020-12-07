from idaapi import *

start_addr = 0x8048000
end_addr = 0x804c000

data = []
for i in range(start_addr,end_addr):
    data.append(Byte(i))

with open('dump_elf','w') as f:
    f.write(''.join(map(chr,data)))
f.close()
