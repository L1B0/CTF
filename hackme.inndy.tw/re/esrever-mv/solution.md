# esrever-mv

## solution1-测信道

4005f0->400fa0(input flag)

b *0x401047

r if *ebp==0



0x61->取反->&0xff->^0xba->

1 7 10 19 29 19 

0x6c->

1 7 10 23 19 19 29

0x31

1 7 10 23 19 19 29

可以观察到，当输入符合flag时，会接受后一个字符（换行），即要输入；

当输入不符合时，后一个字符没有被接收，进入到输出Bad flag，即要输出。

那么就可以侧信道。

![image-20210629220026456](https://i.loli.net/2021/06/29/jMbaxJh8FLQem1c.png)

如下图，IO_flag为ax的值，为1时输出，为0时输入。

```c
__int16 __fastcall sub_400A60(__int64 a1)
{
  __int16 IO_flag; // ax
  int v2; // eax
  __int64 v3; // rdx
  char v5; // [rsp+7h] [rbp-11h]
  unsigned __int64 v6; // [rsp+8h] [rbp-10h]

  v6 = __readfsqword(0x28u);
  IO_flag = *(_WORD *)(a1 + 65544);
  if ( IO_flag )
  {
    if ( IO_flag == 1 )                         // Input flag
    {
      v5 = *(_WORD *)(a1 + 0x1000A);
      v2 = -(sub_440300(1LL, (__int64)&v5) != 1);// printf
    }
    else
    {
      LOWORD(v2) = 0;
    }
  }
  else
  {
    v3 = sub_4402A0(0LL, (__int64)&v5);         // read input
    LOWORD(v2) = -1;
    if ( v3 == 1 )
      LOWORD(v2) = v5;
  }
  if ( __readfsqword(0x28u) != v6 )
    sub_443EB0();
  return v2;
}
```

写gdb脚本，和shell脚本进行逐位爆破。

这flag是真长啊。。。