message = "[REDACTED]"
key = "123456"
c = '473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554'.decode('hex')

key_len = [2,4,7,8]#14,28

r,o,u,x,h=range,ord,chr,"".join,hex

def e(m,k):
 l=len(k);s=[m[i::l]for i in r(l)]
#print s
 for i in r(l):
  a,e=0,""
  for c in s[i]:
   a=o(c)^o(k[i])^(a>>2)
   e+=u(a)
  s[i]=e
#print s
 return x(h((1<<8)+o(f))[3:]for f in x(x(y)for y in zip(*s)))

def d(c,key1,offset):

	flag = ''
				
	a = [ 0 for l in range(len(key1)) ]
	lenk = len(key1)
					
	for k in range(len(c)):
						
		if k%offset < lenk:
			flag += chr( key1[k%offset]^ord(c[k])^(a[k%offset]>>2) )
			a[k%offset] = ord(flag[k])^key1[k%offset]^(a[k%offset]>>2)
		else:
			flag += ' '
	#burp_len
	if len(key1) == 1 and flag.replace(' ','').isalnum():
		print "[*]You got the length. FLAG: {}".format(flag.replace(' ',''))
	#burp_flag
	if flag.replace('_','').replace('{','').replace('}','').isalnum():
		print "key1 = {} key2 = {} flag = {}".format(key1[6],key1[7],flag)				
def burp_len():
	
	for i in [2,4,7,8,14,28]:
		
		#key[0] == ord('t')^0x47
		key = [ord('t')^0x47]
		print "[+]The key length is {} QAQ".format(i)
		d(c,key,i)

if __name__ == '__main__':

	burp_len()
	key_len = 8
	flag = 'tjctf{'
	for i in range(32,127):
		for j in range(32,127):
			
			key = [ ord(flag[k])^ord(c[k]) for k in r(len(flag)) ]
			key.append(i)
			key.append(j)
#print key
			assert len(key) == key_len	
			d( c, key, key_len )
	
	key = [ chr(ord(flag[k])^ord(c[k])) for k in r(len(flag)) ]
	flag = 'tjctf{m4ybe_Wr1t3ing_mY_3ncRypT10N_MY5elf_W4Snt_v_sm4R7}'
	key.append(chr(90))
	key.append(chr(54))
	
	if e(flag,x(key)) == c.encode('hex'):
		print "Right!!!"

#print(e(message,key))
