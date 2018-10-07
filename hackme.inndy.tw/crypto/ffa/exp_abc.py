from z3 import *
from libnum import prime_test as isPrime

a = BitVec('a',265)
b = BitVec('b',265)
c = BitVec('c',265)

m = 282832747915637398142431587525135167098126503327259369230840635687863475396299
M = 349579051431173103963525574908108980776346966102045838681986112083541754544269

#x = (a + b * 3) % m
#y = (b - c * 5) % m
#z = (a + c * 8) % m
x = 254732859357467931957861825273244795556693016657393159194417526480484204095858
y = 261877836792399836452074575192123520294695871579540257591169122727176542734080
z = 213932962252915797768584248464896200082707350140827098890648372492180142394587

#p = pow(flag, a, M)
#q = pow(flag, b, M)
p = 240670121804208978394996710730839069728700956824706945984819015371493837551238
q = 63385828825643452682833619835670889340533854879683013984056508942989973395315

A = eval('x == (a + b * 3) % m')
B = eval('y == (b - c * 5) % m')
C = eval('z == (a + c * 8) % m')

s = Solver()
s.add( UGT(a,pow(2,256,m)),ULT(a,pow(2,257,m)), UGT(b,pow(2,256,m)),ULT(b,pow(2,257,m)), UGT(c,pow(2,256,m)),ULT(c,pow(2,257,m)), A, B, C )

while s.check() == sat:
	if isPrime(s.model()[a].as_long()) and isPrime(s.model()[b].as_long()) and isPrime(s.model()[c].as_long()):
		print(s.model)
		print(s.model()[a].as_long(),s.model()[b].as_long(),s.model()[c].as_long())
	s.add( Or( a != s.model()[a], b != s.model()[b], c != s.model()[c] ) )
else:
	print("Done")
