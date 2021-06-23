#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;
unsigned int passwd = 0xE98F842A;
char str_map[64] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

int sub_4091E0(unsigned int ebx)
{
	unsigned int eax1 = 0xb7aac296, eax2 = 0x5a5a7e05, eax3;
	/*
	__asm__ __volatile__(
	"movl %1, %%eax \n\t;"
	"movl %2, %%ecx \n\t;"
	"xorl %%edx, %%edx \n\t;"
	
	//"decl %%esi \n\t;"
	
	//"loop1: \n\t;"
	//"incl %%esi \n\t;"
	"xorb %%cl, %%ah \n\t;"
	
	"loop2: \n\t;"
	"xorb %%dl, %%al \n\t;"
	"addl $0x434f4445, %%eax \n\t;"
	"movb %%al, %%cl \n\t;"
	"rorl %%cl, %%eax \n\t;"
	"xorl $0x55aa5a5a, %%eax \n\t;"
	"decw %%dx \n\t;"
	"jne loop2 \n\t;"
	
	//"cmpl $0, (%%esi) \n\t;"
	//"jne loop1 \n\t;"
	
	"movl %%eax, %0 \n\t;"
	
	:"=r"(gavin) :"r"(sum),"r"(a) :"%eax","%ecx","%edx","%esi"
	);
	*/
	__asm__ __volatile__(
	"movl %1, %%ebx \n\t;"
	"movl $0xb7aac296, %%eax \n\t;"

	"movb %%al, %%cl \n\t;"
	"roll %%cl, %%ebx \n\t;"
	"xorl %%ebx, %%eax \n\t;"
	"movb %%bh, %%cl \n\t;"
	"rorl %%cl, %%eax \n\t;"
	
	"movl %%eax, %0 \n\t;"
	:"=r"(eax3) :"r"(ebx) :"%eax","%ecx","%ebx");
	//printf("%x %d\n",gavin,gavin==passwd);

	return eax3 == eax2;
	
}

int main()
{
	char input[10] = "0";
	for(unsigned int a=0xffffffff;a>=0;a--)
	{
		
			//printf("%x %c\n",a,0);
		if(sub_4091E0(a))
		{
			printf("%x\n",a);
		}
		if(a == 0) break;
		
	}
	return 0;
}

