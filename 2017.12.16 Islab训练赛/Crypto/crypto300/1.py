

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
print getPrime(2048)
