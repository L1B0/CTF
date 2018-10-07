from pwn import *
import numpy as np

io = remote('hackme.inndy.tw',7707)
#io = process('./fast')

io.recvuntil("Send 'Yes I know' to start the game.")
io.sendline('Yes I know')

result = ''

for i in range(10000):
	
	temp = io.recvuntil("=")[:-1]
	#print temp
	io.recvline()
	temp = temp.strip().split(' ')
	print temp
	
	if temp[1] == '+':
		result += str( np.int32(int(temp[0])) + np.int32(int(temp[2])) )
	if temp[1] == '-':
		result += str( np.int32(int(temp[0])) - np.int32(int(temp[2])) ) 
	if temp[1] == '*':
		result += str( np.int32(int(temp[0])) * np.int32(int(temp[2])) )
	if temp[1] == '/':
		result += str( int(1.0*np.int32(int(temp[0])) / np.int32(int(temp[2])) ) )
	result += '\n'

io.sendline(result) 
io.interactive()
