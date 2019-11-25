from z3 import *

correct = [7,6,8,7,6,7,7,7,7,6]
a = BitVec('a',8)
b = BitVec('b',8)
c = BitVec('c',8)
d = BitVec('d',8)

name_first_1bit = (a & 1) + 5
name_first_5bit = ((a >> 4) & 1) + 5
name_first_2bit = ((a >> 1) & 1) + 5
name_first_3bit = ((a >> 2) & 1) + 5
name_first_4bit = ((a >> 3) & 1) + 5

name_second_1bit = (b & 1) + 1
name_second_5bit = ((b >> 4) & 1) + 1
name_second_2bit = ((b >> 1) & 1) + 1
name_second_3bit = ((b >> 2) & 1) + 1
name_second_4bit = ((b >> 3) & 1) + 1  

name_third_1bit = (c & 1) + 5
name_third_5bit = ((c >> 4) & 1) + 5
name_third_2bit = ((c >> 1) & 1) + 5
name_third_3bit = ((c >> 2) & 1) + 5
name_third_4bit = ((c >> 3) & 1) + 5

name_fourth_1bit = (d & 1) + 1
name_fourth_5bit = ((d >> 4) & 1) + 1
name_fourth_2bit = ((d >> 1) & 1) + 1
name_fourth_3bit = ((d >> 2) & 1) + 1
name_fourth_4bit = ((d >> 3) & 1) + 1 

x = Solver()
x.add( And(a >= ord('a'), a <= ord('z')) )
x.add( And(b >= ord('a'), b <= ord('z')) )
x.add( And(c >= ord('a'), c <= ord('z')) )
x.add( And(d >= ord('a'), d <= ord('z')) )

x.add( (name_first_1bit + name_second_3bit) == correct[0] )
x.add( (name_first_4bit + name_second_4bit) == correct[1] )
x.add( (name_first_2bit + name_second_5bit) == correct[2] )
x.add( (name_first_3bit + name_second_1bit) == correct[3] )
x.add( (name_first_5bit + name_second_2bit) == correct[4] )

x.add( (name_third_1bit + name_fourth_3bit) == correct[5] )
x.add( (name_third_4bit + name_fourth_4bit) == correct[6] )
x.add( (name_third_2bit + name_fourth_5bit) == correct[7] )
x.add( (name_third_3bit + name_fourth_1bit) == correct[8] )
x.add( (name_third_5bit + name_fourth_2bit) == correct[9] )

while x.check() == sat:
	flag = chr(x.model()[a].as_long()) + chr(x.model()[b].as_long()) + chr(x.model()[c].as_long()) + chr(x.model()[d].as_long())
	if flag[-1] == 'p':
		print flag
	x.add( Or( a!=x.model()[a].as_long(), b!=x.model()[b].as_long(), c!= x.model()[c].as_long(), d!= x.model()[d].as_long() ) )