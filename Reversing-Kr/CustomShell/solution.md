# reversing-kr-CustomShell

![image-20210701120658204](https://i.loli.net/2021/07/01/j9TwfWguGn3mx6H.png)

```
AVR System emulator
Use the executable qemu-system-avr to emulate a AVR 8 bit based machine. These can have one of the following cores: avr1, avr2, avr25, avr3, avr31, avr35, avr4, avr5, avr51, avr6, avrtiny, xmega2, xmega3, xmega4, xmega5, xmega6 and xmega7.
```

![image-20210701121050010](https://i.loli.net/2021/07/01/6bQlGJXedpNy8nO.png)

https://qemu-project.gitlab.io/qemu/system/target-avr.html

https://www.mikrocontroller.net/articles/AVR-Simulation

## 安装avr调试环境

### avr studio4

下载链接：http://www.atmel.com/Images/AvrStudio4Setup.exe

### hapsim

下载链接：https://ic.unicamp.br/en/~edson/disciplinas/mc404/2011-2s/anexos/hapsim/introducao_hapsim.html

## 调试

### hapsim

![image-20210811203748279](https://i.loli.net/2021/08/11/5FD9ok2LE4igTjp.png)

## 分析

程序的流程如下：

1. 输入Login，对login进行验证，比较是否位revkr12；

2. 输入passwd，对passwd进行加密后校验（长度为8），加密进行了两次，每次8轮，取不同的key与passwd进行异或，可以在调试的时候一个一个记录下来。然后会求sum(passwd)，并以sum和每个字符在passwd的位置（1~8）确定循环右移的位数，并进行循环右移，最后与一串数据（长度为10，可以dump出来）进行校验。

   1. passwd可以逆向求出来，因为最后校验的数据的第一个字节和最后一个字节对应了sum(passwd)，那么就可以逆向到循环右移环节之前的enc_passwd，然后再根据调试记录的key与enc_passwd异或回去，就可以得到passwd。

3. 登录成功后，根据尝试有以下命令，查看文件内容发现readme文件提示不存在。。。在网上查了下发现这里有问题，然后调试可以发现readme后面还跟了个0x20即空格，在调试的时候patch掉比较的结果即可得到文件内容即flag。

   ```
   whoami
   ls -al
   cat
   cd
   exit
   ```

   目录结构为

   ```
   /etc
   - passwd
   - shadow
   - issue
   /tmp
   - readme
   /var
   - /log
    - syslog
   /bin
   - sh
   - ls
   - cat
   ```

   readme

   ![image-20210811152134409](https://i.loli.net/2021/08/11/hHyYQUAt5nNsOao.png)

关键功能：0x61->0x7f6接收login

701

760比较login：Login: revkr12

76c开始校验passwd

2b5对passwd异或0x4a

310对passwd求和，8位，

31a 加载加密后的9位passwd，

7f7校验返回值，为1通过。



![image-20210810152240943](https://i.loli.net/2021/08/10/roaRtMDZ6cdTCkF.png)



## 参考资料

https://blog.attify.com/flare-4-ctf-write-part-4/

http://blukat29.github.io/2015/09/jff-avreversing/

avr指令: https://www.dianyuan.com/upload/community/2014/01/19/1390113026-80267.pdf