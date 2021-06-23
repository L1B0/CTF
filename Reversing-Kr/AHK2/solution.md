# reversing-kr-AutoHotKey2

## README

提示需要对程序进行修改。
> It should be modified to work properly.

![2118_1](https://i.loli.net/2021/06/23/7PFBpJHnWhtzK3M.png)

![2120_1](https://i.loli.net/2021/06/23/O4qjD5GVTl1raso.png)

## 脱壳

F8->esp hardbreak
![2124_1](https://i.loli.net/2021/06/23/pmZBT4sLjk8vHCc.png)

![2126_2](https://i.loli.net/2021/06/23/J5p7RgOTCq9zHDw.png)

## 分析

根据程序运行报错exe corrupted，在dump出来的程序中搜索该字符串，定位到函数4481E0。

![2122_1](https://i.loli.net/2021/06/23/4MZjNBSC3RcOd9k.png)

![2140_1](https://i.loli.net/2021/06/23/OC1xjZIpioavlzc.png)

## patch1

对程序的前多少个字节进行异或计算一个key，然后与文件末尾的四个字节进行比较。
![2126_2 (1)](https://i.loli.net/2021/06/23/Ds4CL2HVOZtGrpy.png)

![2130_1 (1)](https://i.loli.net/2021/06/23/SORy8CmL51HnuTW.png)

## patch2

以文件末尾[-8:-4]个字节作为偏移，读取文件的16个字节，然后与内置的数据进行比较。
经过搜索可以知道偏移为32800h。

![2132_1](https://i.loli.net/2021/06/23/HPARuvGxt8yCSXQ.png)

![2128_1](https://i.loli.net/2021/06/23/CvuYhoIUAnBi6Fm.png)

## patch_result

![2134_1](https://i.loli.net/2021/06/23/p7ujRWmznSZFxGB.png)

## get_flag：jonsnow

> Jon Snow was the bastard son of Eddard Stark, by a mother whose identify is a source of speculation. He was raised by his father alongside his true-born half-siblings, but joined the Night's Watch when he nears adulthood. He was constantly accompanied by his albino direwolf Ghost.

成功运行程序，如下图。
![2136_1](https://i.loli.net/2021/06/23/E3qyb4NSgGulK5o.png)

经过搜索知道是jonsnow。
![2138_1](https://i.loli.net/2021/06/23/eVOQNfpos3FE2kY.png)