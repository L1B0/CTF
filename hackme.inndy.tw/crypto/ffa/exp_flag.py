from libnum import n2s
import sys   
sys.setrecursionlimit(1000000)

def gcd(a, b):
	if a < b:
		a, b = b, a
	while b != 0:
		temp = a % b
		a = b
		b = temp
	return a


def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

#e1 = a, e2 = b
[e1,e2,c] = [
176268455401080975226023429120782206814426280508931609844850047979724152864469L,
214709966595887251005567190400910974312839914267660095937082916625495667341329L,
216832624293207401424643793061865624482130011199431463053855267329954605238489L]
#p = c1 q = c2
[c1,c2] = [
240670121804208978394996710730839069728700956824706945984819015371493837551238,
63385828825643452682833619835670889340533854879683013984056508942989973395315]
#M = n
n = 349579051431173103963525574908108980776346966102045838681986112083541754544269

s = egcd(e1, e2)
s1 = s[1]
s2 = s[2]
print(s)

if s1 < 0:
	s1 = -s1
	c1 = modinv(c1,n)
if s2 < 0:
	s2 = -s2
	c2 = modinv(c2,n)
m = (pow(c1,s1,n)*pow(c2,s2,n)) % n
print(n2s(m))
print(pow(m,e1,n) == c1)
print(pow(m,e2,n) == c2)

