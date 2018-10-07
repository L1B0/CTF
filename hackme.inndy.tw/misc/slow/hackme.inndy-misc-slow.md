## hackme.inndy-misc-slow

> 题目描述：OMG, It's slow.
>
> nc hackme.inndy.tw 7708

<br>

### 0x00 初探

这道题没有附件，只给了一个nc，连上去后如下图

![](http://wx1.sinaimg.cn/mw690/0060lm7Tly1ftqzhlitgfj30kp024mxc.jpg)

可以知道flag格式为FLAG{\\w+\\}，\\w+\\表示匹配字母，数字，下划线或加号，并且没有小写字母和空格，于是符合要求的字符有

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+_
```

<br>

### 0x01 解题过程

了解了flag格式后，觉得字符范围这么小，应该是要逐字符爆破，但怎样才算正确呢？

google之后了解到有一种叫**时序攻击**的手段，在密码学中是**侧信道攻击**的一种。原理大致是通过分析程序**执行的时间**来推导出正确的密码。

结合题目描述(OMG, It's slow.)来看应该是与时间有关，于是测试延迟。

```shell
#此时的输入是FLAG{ + 'now_char' + '}',长度为7
$ python test_slow.py      
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = A  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = B  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = C  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = D  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = E  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = F  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = G  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = H  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = I  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = J  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = K  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = L  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = M  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = N  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = O  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = P  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = Q  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = R  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = S  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = T  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = U  now_time = 7.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = V  now_time = 17.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = W  now_time = 7.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = X  now_time = 16.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = Y  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = Z  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 0  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 1  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 2  now_time = 7.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 3  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 4  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 5  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 6  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 7  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 8  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = 9  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = +  now_time = 6.0
[+] Opening connection to hackme.inndy.tw on port 7708: Done
now_char = _  now_time = 6.0
```

由于网络的原因，可能会有延迟过长的情况，不过可以通过当前字符的位置和当前延时比较来纠错。

经过分析不难发现，每正确一个字符，延迟加一秒，并且time = pos+1，以此我们可以写出爆破脚本。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

import time
from pwn import *
import numpy
#context.log_level = "debug"

flag = 'FLAG{'
max_time = len(flag)+1
num = len(flag)+1
string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+_'

view = numpy.zeros((50,128))
s = ''
temp = ''
while True:
	for x in string:
		#将已check过的字符标记，节省时间
		if view[num][ord(x)] == 1:
			continue
		view[num][ord(x)] = 1

		io = remote('hackme.inndy.tw',7708)
		io.recvuntil('What is your flag?')
		a = time.time()
		io.sendline(flag+x+'}')
		s = io.recvline()
		#print temp == s
		if temp == '':
			temp = s
		io.close()
		b = time.time()
		print "num = {},now_time = {}, now_char = {}, recv = {},max_time = {}".format(num,math.floor(b-a),x,s,max_time)

		if math.floor(b-a) > max_time:
			flag += x
			num += 1
			max_time += 1
			print flag
			break

		elif math.floor(b-a) < max_time:
			flag = flag[:-1]
			num -=1
			max_time -=1
			print 'wrong,now back!'

	if s != temp:
		print flag
```

经测试，这个脚本要一直爆到出flag所需时间为要很久很久，估计得几个小时，我也没耐心跑完过，跑到后面直接猜出来了。。。