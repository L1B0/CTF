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

img = Image.new("RGB",(150,200))###����һ��5*5��ͼƬ
#pixTuple = (255,0,255,15)###������������ΪR,G,B,A   R���� G:�� B:�� A:͸����
for i in range(150):
	for j in range(200):
		d = data[(i*200+j)*3]
		img.putpixel((i,j),(d,d,d))
img.save("bbb.png")
