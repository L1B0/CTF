import numpy as np


flag = 'abcdefghijklmnopqrstuvwxy'

np.random.seed(12345)
#arr = np.array([ord(c) for c in flag])
#print arr 
other = np.random.randint(1,5,25)
print "[+]other: {}".format(other)
#arr = np.multiply(arr,other)
#print arr
#b = [x for x in arr]

lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]

#c = [b[i]^lmao[i] for i,j in enumerate(b)]

#print(''.join(bin(x)[2:].zfill(8) for x in c))

output = '1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101'
#output1 = [304, 189, 161, 133, 7, 169,291]

s = ''
output1 = []
sum,num = 0,0
v = 0
flag = 0

for i,j in enumerate(output):

	if sum%8 == 0 and flag == 1:
		
		v  = eval('0b'+s)
		if (v^lmao[num])%other[num] != 0:
			output1.append( eval('0b'+s+j) )
			s = ''
			
		else:
			output1.append( v )
			sum += 1
			s = j
		num += 1
		flag = 0
		
	else:
		s+= j
		sum += 1
		flag = 1

#print output1

print "[+]lmao: {}".format(lmao)
#context.log_level = 'debug'

mod = [(lmao[i]^output1[i])%other[i] for i in range(len(output1))]
print "[+]mod==0? {}".format(mod)
output2 = [ chr((lmao[i]^output1[i])/other[i]) for i in range(len(output1)) ]
 
print "[+]flag: {}".format(''.join(output2))
#output3 = [ ofor i in range(25) ]
