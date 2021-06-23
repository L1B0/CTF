# reversing-kr-Twist

32位os调试！

输入abcdefgh

![2096_1](https://i.loli.net/2021/06/23/skdw82zeV6LPqtO.png)

![2100_1](https://i.loli.net/2021/06/23/YJykc8p4UKzgXoa.png)

input[6] ^= 0x36
input[6] += 0x20
![2102_1](https://i.loli.net/2021/06/23/GdvEI23l6QhLXce.png)

![2104_1](https://i.loli.net/2021/06/23/g3kZNWVY9ve5HzF.png)

第一个check
![2106_1](https://i.loli.net/2021/06/23/LTEVsZejQfqh1Gx.png)

![2108_1](https://i.loli.net/2021/06/23/jJz7uHMhImaeCwA.png)

'g'^0x36=0x51
![2110_1](https://i.loli.net/2021/06/23/Bw6guV192X5kzKb.png)

ror(input[0],6) == 0x49 ==> input[0]=82='R'
rol(input[0],4)
xor(input[0],0x34)
![2112_1](https://i.loli.net/2021/06/23/juwoQpaTx15CL7J.png)

![2114_1](https://i.loli.net/2021/06/23/l8wBGnm2NKTodAR.png)

xor(input[0],0x12)
xor(input[2],0x77) == 0x35 ==> input[2]='B'
xor(input[1],0x20) == 0x69 ==> input[1]='I'
xor(input[3],0x21) == 0x64 ==> input[3]='E'
xor(input[4],0x46) == 0x8 ==> input[4]='N'
rol(input[5],4) == 0x14 ==> input[5]='A'
RIBENA

## 参考资料

https://bbs.pediy.com/thread-252264.htm