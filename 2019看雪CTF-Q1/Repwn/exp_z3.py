from z3 import *
from string import *


solver = Solver()
a = [Int('a%d'%i) for i in range(8)]

for i in range(8):
	solver.add( Or( And((a[i]+48)<=ord('9'), (a[i]+48)>=ord('0')), And((a[i]+48)<=ord('z'), (a[i]+48)>=ord('a')), And((a[i]+48)<=ord('Z'), (a[i]+48)>=ord('A') )) )

#v1 = a[3] + 1000 * a[0] + 100 * a[1] + 10 * a[2]
#v2 = a[5] + 10 * a[4]

#v3 = a[7] + 10 * a[6]

solver.add( (2 * (a[3] + 1000 * a[0] + 100 * a[1] + 10 * a[2] + a[5] + 10 * a[4])) == 4040)
solver.add( (3 * (a[5] + 10 * a[4]) / 2 + 100 * (a[7] + 10 * a[6])) == 115)
solver.add( (a[3] + 1000 * a[0] + 100 * a[1] + 10 * a[2] - 110 * (a[7] + 10 * a[6])) == 1900)

while solver.check() == sat:
	m = solver.model()
	solver.add( Or(a[0]!=m[a[0]].as_long(),a[1]!=m[a[1]].as_long(),a[2]!=m[a[2]].as_long(),a[3]!=m[a[3]].as_long(),a[4]!=m[a[4]].as_long(),a[5]!=m[a[5]].as_long(),a[6]!=m[a[6]].as_long(),a[7]!=m[a[7]].as_long() ) )
#	print m
	s = ''
	for i in range(8):
		s += chr(m[a[i]].as_long()+48)
	print s
