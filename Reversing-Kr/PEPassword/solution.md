# Reversing-Kr-PEPassword

通过运行程序，输入aaaaaaa，然后用cheatengine搜索字符串定位输入所在的内存地址。
然后在x32dbg里面对该地址下硬件访问断点，从而直接到达关键代码。

程序首先会对输入进行计算一个校验码，如下图。
![2198_1](https://i.loli.net/2021/06/23/bC9lkZdjO3NGxvV.png)

具体代码如下，用内联汇编爆破也不可能，陷入僵局。。。
![2200_1](https://i.loli.net/2021/06/23/ERAmhwogtcPjYJZ.png)

![2190_1](https://i.loli.net/2021/06/23/WEtvXgCen2pNoIU.png)

![2192_1](https://i.loli.net/2021/06/23/3Emsr1Bqv8WwFaf.png)

然后看别人的wp知道后面还有进行解密代码的部分，这里直接在校验时patch寄存器eax即可。
之后到了下图所示，esi即输入，在进入40921f之前，进行两次校验码计算，分别给ebx和eax保存。
然后利用eax与401000异或进行代码解密。
edi初始为401000，于是从original.exe和程序内存401000分别拿出前8个字节的内容，分别异或回去。
得到初始两次寄存器eax的值，然后爆破第一次的ebx，即可得到在解密入口前的eax和ebx值。

在进入40921f之前patch寄存器eax和ebx，然后F9即可得到password。

![2202_1](https://i.loli.net/2021/06/23/jHaiUEeZsI7uOVQ.png)

但是好奇之后flag是怎么输出的，于是又跟着调试了一下，原来是代码解密之后就有了正确的异或数据。

![2204_1](https://i.loli.net/2021/06/23/s4LaqVSY9f1iJu2.png)

![2206_1](https://i.loli.net/2021/06/23/LXUswEcifBAgFtn.png)

脚本如下，由于只进行了第一次和第二次循环的校验，所以会有两个结果，都试一下即可。

```python
r11t@ubuntu:~/Desktop$ cat exp.cpp
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;
unsigned int passwd = 0xE98F842A;
char str_map[64] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

int sub_4091E0(unsigned int ebx)
{
    /*
 >>> 0xB6E62E17^0x014cec81
3081421462
>>> hex(_)
'0xb7aac296'
>>> 0x0D0C7E05^0x57560000
1515879941
>>> hex(_)
'0x5a5a7e05'
>>> 
    */
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
r11t@ubuntu:~/Desktop$ g++ -m32 exp.cpp -o exp
r11t@ubuntu:~/Desktop$ ./exp 
c263a2cb
a1beee22

```
