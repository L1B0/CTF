from z3 import *

array = [164,25,4,130,126,158,91,199,173,252,239,143,150,251,126,39,104,104,146,208,249,9,219,208,101,182,62,92,6,27,5,46]

def find_num():
	num = BitVec('num',64)
	flag = "FLAG{}"
	b = 0
	s = Solver()
	
	#s.add( ord(flag[0]) ==  (( (num&0x7f)^b^array[0] ) & 0x7f) )
	#b ^= array[0]
	#num >>= 1
	#s.add( ord(flag[1]) ==  (( (num&0x7f)^b^array[1] ) & 0x7f)  )
	
	for i in xrange(32):
		if i < 5:
			s.add( ord(flag[i]) ==  (((num&0x7f)^b^array[i]) & 0x7f) )
		elif i == 31:
			s.add( ord(flag[5]) ==  (((num&0x7f)^b^array[i]) & 0x7f) )
		else:
			s.add(
				Or(
					And(
						(((num&0x7f)^b^array[i]) & 0x7f) <= ord("Z"),
						(((num&0x7f)^b^array[i]) & 0x7f) >= ord("A")
					),
					(((num&0x7f)^b^array[i]) & 0x7f) == ord(" ") 
				)
			)
		b ^= array[i]
		num >>= 1
	
	if s.check() == sat:
		return s.model()
def __main__():
	num = 3658134498
	flag = ''
	b = 0
	for i in range(len(array)):
         flag += chr( (num^b^array[i])&0xff )
         b ^= array[i]
         num >>= 1
	print(flag)
__main__()
