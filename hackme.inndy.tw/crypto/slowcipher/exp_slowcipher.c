#include<stdio.h>
#include<stdlib.h>
#include<string.h>

long long v7 = 0xDEADBEEF01234567;
int v6 = 0;
unsigned long long v11=7;

void check_passwd(char *passwd){
	
	for(int i=0;i<=strlen(passwd);i++){
		char pd;
		if(i == strlen(passwd)) pd = 0;
		else pd = passwd[i];
		long long temp = (777 * pd) ^ ( 3333 * ((0x777777 * v7 + 12345) & 0x7FFFFFFFFFFFFFFF) ), temp_l = ((unsigned long long)temp)>>13;
		printf("temp = %lld temp>>13 = %lld\ntemp^(temp>>13) = %lld\n",temp,temp_l,temp_l^temp);
		v7 = ( temp_l ^ temp ) + 0x5555555555555555;
		printf("for v7 = %llu\n",v7);
		for(int j=0;j<(pd+66);j++) 
			v7 = (0x777777 * v7 + 12345) & 0x7FFFFFFFFFFFFFFF;
		printf("for1 v7 = %lld\n",v7);
	}
	printf("v7 = %lld\n",v7);
	puts("check_passwd Finished\n");
	return ;
}

void encode_flag(char *flag){

	puts(flag);
	char encode_f[50]={0};
	printf("%d\n",strlen(flag));
	for(int i=0;i<strlen(flag);i++){
		
		int v16 = flag[i];
		unsigned char encode=flag[i];
		
		for(int j=0;j<v11;j++){
			v7 = (0x777777 * v7 + 12345) & 0x7FFFFFFFFFFFFFFF;
		}
		if(v6){
			unsigned long long t = (21 * v11 * 0xCCCCCCCCCCCCCCCD),tt = t>>64;
			printf("resl = %llu %llu\n",t,tt);
			encode_f[i] = (encode^v7)&0xff;
		}
		else{
			encode = v7^v16;
			v11 = ( ( (21 * ((unsigned long long)v11) * 0xCCCCCCCCCCCCCCCDL) >> 64 ) >> 3 )^encode;
			encode_f[i] = encode;
		}
		printf("v11 = %llu\n",v11);
		printf("encode_f: %d\n",encode_f[i]);
	}
	return ;
}

int main(int argc, char *argv[]){
	
	if(argc < 4) return 0;
	int mymode = atoi(argv[1]);
	char *mypasswd = argv[2], *myinput = argv[3];
	puts(mypasswd);
	puts(myinput);
	v6 = (mymode&0xdf)!=68 ? 1 : 0;
	check_passwd(mypasswd);
	encode_flag(myinput);
	return 0;
}
	
