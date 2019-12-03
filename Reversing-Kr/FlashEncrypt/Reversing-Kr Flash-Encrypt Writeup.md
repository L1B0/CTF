# Reversing-Kr Flash-Encrypt Writeup

> [题目及脚本](https://github.com/L1B0/CTF/tree/master/Reversing-Kr/FlashEncrypt)

## 解题思路

题目是一个swf(shock wave flash)类型的文件，于是去网上找了个[反编译flash的程序JPEXS]( https://www.52pojie.cn/thread-584213-1-1.html )。

不得不说，真的好用:-)

用**JPEXS**打开swf文件，在设置一栏勾选**自动反混淆**，不然看到的代码会怀疑人生。

可以看到有6个button，每个button都有相应的点击事件。

![QMVdW4.png](https://s2.ax1x.com/2019/12/03/QMVdW4.png)

![QMVIOI.png](https://s2.ax1x.com/2019/12/03/QMVIOI.png)

![QMV70P.png](https://s2.ax1x.com/2019/12/03/QMV70P.png)

![QMVqk8.png](https://s2.ax1x.com/2019/12/03/QMVqk8.png)

![QMVHTf.png](https://s2.ax1x.com/2019/12/03/QMVHTf.png)

![QMVTmt.png](https://s2.ax1x.com/2019/12/03/QMVTmt.png)

逻辑其实很简单，**spw**即文本框的输入，相等就跳转到另一个frame进行后续的操作。

在文件一栏**另存为exe**，一个一个输入即可得到最终的key。

结果如下

![QMZltO.png](https://s2.ax1x.com/2019/12/03/QMZltO.png)

