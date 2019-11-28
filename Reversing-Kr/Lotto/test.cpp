#include<stdio.h>

#include <stdlib.h>
#include<time.h>

 
int main()
{
	unsigned int v0 = 0x000000005DDF5C54;
	srand(v0);
	for(int i=0;i<6;i++)
	{
		printf("%u\n",rand()%100);
	}
	
	return 0;
} 
