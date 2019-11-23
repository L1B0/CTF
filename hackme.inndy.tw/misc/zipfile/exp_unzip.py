import os
import zipfile
from copy import copy

nowdir = '/root/Desktop/test/zipfile.zip'
targetzfile = zipfile.ZipFile(nowdir,'r')
flag = ''

for i in range(256):
	
	# 0 -> 00000000
	targetName = bin(i)[2:].zfill(8)
	# 01010101 -> 0/1/0/1/0/1/0/1
	targetName = '/'.join(targetName)

	print "[*] target = %d"%i
	
	littleFlag = []
	
	for info in targetzfile.infolist():
		
		#print targetName,info.filename[-19:]	
		if targetName != info.filename[-18:-3]:
			continue
			
		print "Find it~"

		# read 0/1/0/1/0/1/0/1PK and creat temp file
		data = targetzfile.read(info)
		f = open('./temp','w+b')
		f.write(data)
		f.close()
		
		target = './temp'
		# print target
		
		# first unzip	
		zfile = zipfile.ZipFile(target,'r')
		
		for filename in zfile.namelist():
			
			#print target,filename		
			data = zfile.read(filename)
			f = open('./temp2','w+b')
			f.write(data)
			f.close()
		
		# second unzip
		zfile = zipfile.ZipFile('./temp2','r')
		d = []
	
		for info in zfile.infolist():
			d.append(zfile.read(info))
		
		d = [ map(ord,i) for i in d ]
		print d

		s = []
		#s = copy(littleFlag)
		#print littleFlag,s
		for i in range(len(d[0])):
			t = 0
			for j in range(len(d)):
				t ^= d[j][i]

			#print chr(t)
			#print littleFlag,s
			if littleFlag == []:
				s.append(t)
			else:
				s[i] ^= t 
		flag += '\'' + ''.join(map(chr,s))+'\','
		#littleFlag = copy(s)
	#flag += ''.join(map(chr,littleFlag))
	flag += ']\n'
		
print flag
