# reversing-kr-Adventure



![image-20210624103148713](https://i.loli.net/2021/06/24/us7dTD5hLt8VRPx.png)

![image-20140724103758087](https://i.loli.net/2021/06/24/cL1oONBVieylpS2.png)



gameover是图片，无法搜索。

![image-20210624105144955](https://i.loli.net/2021/06/24/bMWBzRAJFYTyE6s.png)

ida搜索bullte字符串，16进制串为62 00 75 00

![image-20210803100949800](https://i.loli.net/2021/08/03/rvu1Xg25fFxWqH7.png)

随机函数

![image-20210803211627169](https://i.loli.net/2021/08/03/SIb5GfwYmdQWJiU.png)

由4093e0



![image-20210803153830168](https://i.loli.net/2021/08/03/ihRwNBgdEWoSumI.png)

![image-20210803154035162](https://i.loli.net/2021/08/03/JfdjS7RkChZHM2g.png)

game over 5e7b

4123

score=3

eax=1 ecx=4

eax=210 ecx=4

score=5

![image-20210803151839404](https://i.loli.net/2021/08/03/RLjNJrxwPtlnUYy.png)

7

![image-20210803152454458](https://i.loli.net/2021/08/03/BPTv6N4EL9qaubd.png)

![image-20210803152739157](https://i.loli.net/2021/08/03/mVoOaLUXMq2B4H6.png)

score=9

![image-20210803151621170](https://i.loli.net/2021/08/03/6grYqCTvywao2xZ.png)



## 调试

### debug while lanuch

![image-20210804100951190](https://i.loli.net/2021/08/04/bDkJPn2ulIYAhsL.png)

```powershell
PS C:\Program Files (x86)\Windows Kits\10\Debuggers\x86> .\plmdebug.exe /enableDebug Microsoft.Adventure.CPP_1.0.0.0_x86__8wekyb3d8bbwe "D:\软件\x64dbg\release\x32\x32dbg.exe"
Package full name is Microsoft.Adventure.CPP_1.0.0.0_x86__8wekyb3d8bbwe.
Enable debug mode
SUCCEEDED
PS C:\Program Files (x86)\Windows Kits\10\Debuggers\x86> .\plmdebug.exe /disableDebug Microsoft.Adventure.CPP_1.0.0.0_x86__8wekyb3d8bbwe
Package full name is Microsoft.Adventure.CPP_1.0.0.0_x86__8wekyb3d8bbwe.
Disable debug mode
SUCCEEDED
```

### debug while running

打开程序，快速打开x32dbg，附加上去，第一次要下好断点，第二次就会成功停下。

4032e0

随机种子

![image-20210804103559422](C:/Users/l1b0/AppData/Roaming/Typora/typora-user-images/image-20210804103559422.png)

![image-20210804103524975](https://i.loli.net/2021/08/04/e7S6gzFVJPK8CqA.png)

xor dword ptr ds:[edi+ecx*8+88],eax 



## 实现自动打怪(flag1结果是错的2333)



![image-20210804152228686](https://i.loli.net/2021/08/04/S6jk4IRdwoXQCe8.png)

5d50->get_flag

![image-20210805101332143](https://i.loli.net/2021/08/05/ItgzCADKlpy1njw.png)