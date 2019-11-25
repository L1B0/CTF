#coding=utf-8
from PIL import Image

f = open('data.txt','r').readlines()
data = []

for i in f:
	#print i[10:58]
	t = i[10:58].split(' ')
	for j in t:
		if j == 'FF':
			data.append(0xff)
		elif j == '00':
			data.append(0x00)

print len(data)

img = Image.new("RGB",(150,200))###创建一个5*5的图片
#pixTuple = (255,0,255,15)###三个参数依次为R,G,B,A   R：红 G:绿 B:蓝 A:透明度
for i in range(150):
	for j in range(200):
		d = data[(i*200+j)*3]
		img.putpixel((i,j),(d,d,d))
img.save("bbb.png")
