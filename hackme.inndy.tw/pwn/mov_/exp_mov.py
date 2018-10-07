from pwn import *
#context.log_level = 'debug'

flag = ''
while 1:
	for i in range(32,126):
		io = process('./mov')
		elf = ELF('./mov')
		io.sendlineafter(':',flag+chr(i))
		temp = io.recvline()
		
		if temp [1] == 'G':
			flag += chr(i)
			print flag
			break
		io.close()	
	if flag != '' and flag[-1] == '}':
		break
