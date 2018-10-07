
assert len(flag) == 32

from libnum import s2n
from primefac import nextprime
from random import randint
from os import urandom

def getPrime(n):
    n /= 8
    m4x = 1
    while(n):
        m4x = m4x << 8
        n -= 1
    m4x -= 1
    m1n = (m4x + 1) >> 4
    tmp = randint(m1n,m4x)
    return nextprime(tmp)

#产生256个字节的字符串，前面是
def padding(s):
    return s + urandom(abs(256 - len(s)))



def append(m):
    p = getPrime(2048)
    print p
    q = getPrime(2048)
    n = p * q
    result = ["%s\n" % str(n)]
    pm = padding(flag)

    for i in range(32):
        e = getPrime(32)
        c = pow(s2n(pm), e, n)
        result.append("%s->%s\n" % (str(e), str(c)))
    return "".join(result)

append(111)
