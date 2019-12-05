# Reversing-Kr AutoHotKey1 Writeup

> [题目及脚本](https://github.com/L1B0/CTF/tree/master/Reversing-Kr/AutoHotKey1)

## 解题思路

首先看下README，提示最终flag由两部分**DecryptKey**和**EXE's Key**的**逆md5值**组成。

> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
>
> AuthKey = un_md5(DecryptKey) + " " + un_md5(EXE's Key)
>
> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
>
> Ex:)
>  DecryptKey = 1dfb6b98aef3416e03d50fd2fb525600
>  EXE's  Key = c944634550c698febdd9c868db908d9d
>  => AuthKey = visual studio
>
> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
>
> By Pyutic

用PEID看下程序，显示有UPX壳，可以通过`upx -d`或者**ESP定律**脱壳。

![Q8mAEj.png](https://s2.ax1x.com/2019/12/05/Q8mAEj.png)

接下来用ida分析脱壳后的程序，打开后发现程序很大，无从下手。

运行一下脱壳后的程序提示`EXE corrupted`。

![Q8nTmD.png](https://s2.ax1x.com/2019/12/05/Q8nTmD.png)

那就先运行脱壳之前的程序，有个输入框，一个OK和Cancel按钮，随便输入然后点击OK发现程序直接退出了。

![Q8upnS.png](https://s2.ax1x.com/2019/12/05/Q8upnS.png)

这里提供一个对于这种有按钮，有文本框的逆向思路。

程序通过是通过调用`GetDlgItem`函数，以各个组件的id为索引获取相应的资源（文本或响应函数）。

我们可以用`Resource Hacker`查看脱壳后的程序的各个框的id，如下图。

![Q8uUBD.png](https://s2.ax1x.com/2019/12/05/Q8uUBD.png)

可以看到文本框的id为**201**。

回到ida，在`Imports`表中搜索`GetDlgItem`，可以看到相应地址为`0x45A330`。

![Q8KHJA.png](https://s2.ax1x.com/2019/12/05/Q8KHJA.png)

双击进去通过`x`查看交叉引用。

![Q8MPWn.png](https://s2.ax1x.com/2019/12/05/Q8MPWn.png)

进入函数`DialogFunc`，可以看到在下图位置引用了id为201的资源。

![Q8MlS1.png](https://s2.ax1x.com/2019/12/05/Q8MlS1.png)

那么就开始动态调试，注意这里由于脱壳后的程序运行有问题，故调试对象为源程序。

首先来到程序入口，

![Q8M2kQ.png](https://s2.ax1x.com/2019/12/05/Q8M2kQ.png)

F8（单步步过）一下，esp寄存器变红，在esp寄存器右键选择HW break[esp]，即hardware break esp，在esp地址处下硬件断点。

![Q8Mqk4.png](https://s2.ax1x.com/2019/12/05/Q8Mqk4.png)

F9（执行到断点）一下，到达第一个红色箭头处，可以看到不远处就有一个大跳转。

![Q8QuB8.png](https://s2.ax1x.com/2019/12/05/Q8QuB8.png)

点击`00471BD6`，F4（执行至选择处）一下，然后F8（单步步过），跳到`00442B4F`。

至此完成UPX的解压壳过程，以上为**ESP定律方法**脱壳。

这里为了保险起见，在api`GetDlgItem`处下断点，在上面的Import表中可以看到该api是在USER32的库中。

在olldbg中`Alt+E`查看执行模块，在相应位置右键选择**查看名称**。

![Q8lYPH.png](https://s2.ax1x.com/2019/12/05/Q8lYPH.png)

可以找到`GetDlgItem`地址为`77754800`，双击后F2下断点。

![Q8l0qf.png](https://s2.ax1x.com/2019/12/05/Q8l0qf.png)

然后F9运行程序，会看到程序停在`GetDlgItem`，在右下角的栈上可以看到相应的参数数值。

![Q8l5ZT.png](https://s2.ax1x.com/2019/12/05/Q8l5ZT.png)

继续F9，直到弹出程序框，输入1234后点击OK。

可以看到程序正在获取id为201的资源，F8执行至retn，看看它会返回到哪。

![Q81kQI.png](https://s2.ax1x.com/2019/12/05/Q81kQI.png)

如下图，可以看到返回至`00425F39`。

![Q81tTU.png](https://s2.ax1x.com/2019/12/05/Q81tTU.png)

这里相应的ida的伪码就不放了，我也没看懂后续干了啥。

接着继续F8，在经过函数`sub_401D9F`后查看ecx的值发现有点东西。

![Q83V39.png](https://s2.ax1x.com/2019/12/05/Q83V39.png)

把这个md5值去[cmd5](https://www.cmd5.com/)查一下，发现是`pawn`。

但题目需要两个字符串，这个md5值感觉是`exe's key`，因为是对输入进行的校验，但我也没看到哪进行了`Decrypt`的操作。

把这个md5值输入到程序的输入框，结果如下图，点确定后就没了，没了，了。。。

![Q88OQs.png](https://s2.ax1x.com/2019/12/05/Q88OQs.png)

去网上看了看别人的题解，发现最开始那个脱壳程序报的`EXE corrupted`有点东西。

在ida的字符串中搜索可以看到这个字符串被两个函数引用了。

![Q8Gj9e.png](https://s2.ax1x.com/2019/12/05/Q8Gj9e.png)

对两个地址下断点，执行程序后会发现程序停在了`sub_4481E0`。

看下对应的伪码，经过了`sub_4508C7`的校验。

![Q8Jnun.png](https://s2.ax1x.com/2019/12/05/Q8Jnun.png)

于是F7（单步步入）跟进去，然后不断F8，可以看到寄存器出现了md5。

![Q8YFq1.png](https://s2.ax1x.com/2019/12/05/Q8YFq1.png)

这个函数应该就是一个readme所说的解密函数。