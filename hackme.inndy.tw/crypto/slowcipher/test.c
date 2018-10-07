#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//__Author__ = 'L1B0'

int main()
{
	printf("%d\n",sizeof(long long));
	unsigned long long a=(21*7*0xCCCCCCCCCCCCCCCDL),b = a>>64;
	printf("%llu %llu\n",a,b);
	return 0;
}
