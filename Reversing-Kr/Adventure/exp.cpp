#include<stdio.h>
#include<stdlib.h>

unsigned int myrand(unsigned int a,unsigned int b)
{
	unsigned int result = a + rand()%(b-a+1);
	//if(b != 50)
		//printf("0x%x\n",result);
	
	return result;
}

unsigned int myrol(unsigned int a,unsigned int b)
{
	a = (a<<b)+(a>>(32-b));
	return a;
}

int main()
{
	srand(0x64);
	
	unsigned int key1[8] = {0x98A96C7,0x5A0DC398,0xB773AAB,0xBE8806A0,0x0D01612BE,0x2873543B,0x4461496E,0x09C0BED2};
	unsigned int key2[8] = {0x646EB4AD,0xCA973FF2,0x0F5B9A83,0x0EE15974E,0x61A2771B,0x0DEB785ED,0x52DBA003,0x9EBE0B4E};
	unsigned int num=0;
	unsigned int data[10] = {0};
	while(1)
	{
		if(myrand(1,50) == 5)
		{
			//puts("genxin!");
			unsigned int a,b,c,d;
			a = myrand(0,0x4c3);
			b = myrand(1,2);
			c = myrand(1,4);
			d = myrand(4,10);
			//printf("%d %d %d %d\n",a,b,c,d);
			
			data[c*2-2] ^= b;
			data[c*2-1] ^= b;
			
			if(num == 0xddb-1)
			{
				for(unsigned int i=0;i<8;i++)
				{
					data[i] ^= key1[i];
					//printf("%x\n",data[i]);
					printf("%c%c%c%c",data[i]&0xff,(data[i]>>8)&0xff,(data[i]>>16)&0xff,(data[i]>>24)&0xff);
				}
				//printf("\n");
			}
			else if(num == 0x31159cd-1)
			{
				for(unsigned int i=0;i<8;i++)
				{
					data[i] ^= key2[i];
					//printf("%x\n",data[i]);
					printf("%c%c%c%c",data[i]&0xff,(data[i]>>8)&0xff,(data[i]>>16)&0xff,(data[i]>>24)&0xff);
				}
				printf("\n");
			}
			
			data[c*2-2] = myrol(data[c*2-2],c);
			data[c*2-1] = myrol(data[c*2-1],d);
			
			//printf("%x %x\n",data[c*2-2],data[c*2-1]);
			//puts("----");
			num ++;
		}
		if(num == 0x31159cd) break;
	}
	return 0;
}
