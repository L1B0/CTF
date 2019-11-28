#include<stdio.h>
/*
Python2
>>> -1536092243306511225&0xffffffffffffffff
16910651830403040391L
>>> hex(_)
'0xeaaeb43e477b8487L'
>>> from decimal import Decimal
>>> for i in range(0x10000):
...     t = Decimal(i<<64) + 0xeaaeb43e477b8487L
...     if t % 26729 == 0:
...             print t
...
253087792599051741660295
746150814945234346804359
>>> 253087792599051741660295%26729
0L
>>> 253087792599051741660295/26729
9468659231510783855L
*/
int main()
{
	long long a;
	a = 9468659231510783855;
	
	printf("%lld %lld\n",a,a*26729);
	return 0;
 } 
