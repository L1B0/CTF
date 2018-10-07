## 安恒杯-linkCTF-13-re100

> 我先吐槽一句，这题真是巨坑==

#### Step1: 脱UPX

首先file一下，发现有upx壳，这是第一关。

二话不说`upx -d Youngter-drive.exe `脱掉。

![](http://wx4.sinaimg.cn/mw690/0060lm7Tly1fubbwetbapj30s602mmxx.jpg)

#### Step2: 修复F5

然后拖进IDA看源码，主函数如下

![](http://wx1.sinaimg.cn/mw690/0060lm7Tly1fubc0e29l3j30v90biq4n.jpg)

然后这点一点那点一点发现`StartAddress`里有猫腻，跟进去发现关键函数`sub_411940`无法F5，提示`positive sp value has been found`

![](http://wx2.sinaimg.cn/mw690/0060lm7Tly1fubc47saiej30bf04rglo.jpg)

出现这个报错的原因是堆栈不平衡，我们可以通过修改`sp value`使堆栈平衡。

> IDA中Options->General选中Stack pointer可以查看堆栈指针

可以看到，就是因为`411A04`处堆栈指针为`-4`导致无法F5，`Alt+K`可以修改此处的`sp value`

![](http://wx1.sinaimg.cn/mw690/0060lm7Tly1fubch1qlyfj30tp07w3zt.jpg)

修改之后如下图，此时堆栈平衡，可以F5。

![](http://wx2.sinaimg.cn/mw690/0060lm7Tly1fubcj8el7mj30v507k3zp.jpg)

然后就可以看到关键函数`sub_411940`的源码

![](http://wx3.sinaimg.cn/mw690/0060lm7Tly1fubcl4n5kej30my0codh2.jpg)

#### Step3: 逆向解密

这个函数相当于一个加密，逻辑很简单，先判断是否是**字母**，如果不是直接终止程序；之后判断如果是**大写字母**则进行替换，**小写字母**进行另一种替换。

加密完成之后和字符串off_418004进行明文比较，相等即正确。

看到这里我兴奋的一批，直接写脚本跑一发，结果发现交了贼多次都不对。。。

后来注意到main函数写了一个多线程(双线程)，然而自己也还不会写多线程，于是疯狂百度函数的作用，才有了上面第二张图主函数的简单注释。

仔细分析会注意到，线程hObject是进行加密，线程v1就是减个下标dword\_418008。而dword\_418008初始值为0x1d即29，这相当于如果dword\_418008是奇数，进行加密，如果是偶数，密文和明文相同。

之后还有个坑，下标从29开始的话意味着输入长度有30，而在函数`sub_411880`进行check时只比较前29个字符，相等即正确。那么我们只需还原明文的前29位，加上一个任意字母即可。

#### exp如下

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'L1B0'

off_418000 = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm\0"

off_418004 = "TOiZiZtOrYaToUwPnToBsOaOapsyS"
print len(off_418004),len(off_418000)

def decode(a):

	flag = ""

	for i in range(len(a)):
		if i %2 == 0:
			flag += a[i]
			continue
		for j,k in enumerate(off_418000):
			if a[i] == k:
				print i,j
				if chr(j+38).isupper():
					flag += chr(j+38)
				else:
					flag += chr(j+96)
				break 
	
	return flag

def encode(flag):
	
	cipher = ""
	for j,i in enumerate(flag):
		if j %2 == 0:
			cipher += i
			continue
		if ord(i) < ord('a') or ord(i) > ord('z'):
			cipher += off_418000[ord(i)-38]
		else:
			cipher += off_418000[ord(i)-96]
	return cipher 

if __name__ == "__main__":
	flag = off_418004
	flag = decode(flag)
	print flag
	cipher = encode(flag)

	print cipher == off_418004
```

> Flag: ThisisthreadofwindowshahaIsES加一个任意字母
>
> 如：ThisisthreadofwindowshahaIsESE